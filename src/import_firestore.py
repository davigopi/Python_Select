import json
import os
import firebase_admin
from firebase_admin import credentials, firestore
from src.var import *
from src.read_salve import Read_salve


read_salve = Read_salve()

# ============================================================
# CONFIGURAÇÕES
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAMINHO_CREDENCIAL = os.path.join(BASE_DIR, "config", "senha.json")
CAMINHO_DADOS = os.path.join(BASE_DIR, "dados_tratados.json")

COLLECTION_NAME = grupo


# ============================================================
# Conecta ao Firestore
# ============================================================

def conectar_firestore():
    if not firebase_admin._apps:
        cred = credentials.Certificate(CAMINHO_CREDENCIAL)
        firebase_admin.initialize_app(cred)
    return firestore.client()


# ============================================================
# Carrega JSON
# ============================================================


def read_arq(path_file):
    read_salve.path_file = path_file
    dados = read_salve.to_read()

    if not isinstance(dados, list):
        raise ValueError("O JSON precisa ser uma LISTA de objetos")

    return dados


# ============================================================
# Tratamento opcional de tipos
# ============================================================

def tratar_tipos(item):
    # Converter alguns campos importantes para número
    if "prazo" in item:
        item["prazo"] = int(item["prazo"])

    if realizadas in item:
        item[realizadas] = int(item[realizadas])

    if a_realizar in item:
        item[a_realizar] = int(item[a_realizar])

    return item


# ============================================================
# Envia para Firestore
# ============================================================

def enviar_para_firestore(db, dados):
    collection_ref = db.collection(COLLECTION_NAME)

    batch = db.batch()
    contador = 0
    total_enviado = 0

    for item in dados:

        item = tratar_tipos(item)

        # ID controlado: grupo_prazo
        doc_id = f"{item[grupo]}"
        doc_ref = collection_ref.document(doc_id)

        batch.set(doc_ref, item)

        contador += 1
        total_enviado += 1

        # Commit a cada 500 operações
        if contador == 500:
            batch.commit()
            print(f"✔️ {total_enviado} registros enviados...")
            batch = db.batch()
            contador = 0

    if contador > 0:
        batch.commit()
        print(f"✔️ {total_enviado} registros enviados...")

    print("🚀 Finalizado envio para Firestore!")


def Import_firestore(path_arq):
    print("🔌 Conectando ao Firestore...")
    db = conectar_firestore()

    print("📦 Carregando dados...")
    dados = read_arq(path_arq)

    print(f"🚀 Enviando {len(dados)} registros...")
    enviar_para_firestore(db, dados)

    print("✅ Importação concluída com sucesso!")


# if __name__ == "__main__":
#     main()
