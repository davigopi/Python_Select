import json
from firebase_admin import credentials, firestore, initialize_app

# Caminho do arquivo de credenciais do Firebase
# Esse arquivo é baixado no Firebase Console (Service Account)
CAMINHO_CREDENCIAL = "serviceAccountKey.json"

# Nome da collection no Firestore
COLLECTION_NAME = "users"

# Caminho do arquivo JSON que será importado
CAMINHO_JSON = "dados.json"


# ============================================================
# Inicializa a conexão com o Firebase / Firestore
# Essa função deve ser chamada apenas uma vez
# Retorna o cliente do Firestore para ser usado nas operações
# ============================================================
def conectar_firestore():
    cred = credentials.Certificate(CAMINHO_CREDENCIAL)
    initialize_app(cred)
    return firestore.client()


# ============================================================
# Lê o arquivo JSON do disco
# Espera um JSON no formato de lista de objetos
# Retorna uma lista de dicionários Python
# ============================================================
def carregar_json():
    with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# Envia os dados para o Firestore
# Cada item da lista vira um documento na collection
# Usa batch para enviar tudo de forma rápida
# Se o item tiver campo "id", ele vira o ID do documento
# Caso contrário, o Firestore gera o ID automaticamente
# ============================================================
def enviar_para_firestore(db, dados):
    batch = db.batch()
    collection_ref = db.collection(COLLECTION_NAME)

    for item in dados:
        doc_id = item.get("id")

        if doc_id:
            doc_ref = collection_ref.document(str(doc_id))
        else:
            doc_ref = collection_ref.document()

        batch.set(doc_ref, item)

    # Executa o envio em lote
    batch.commit()


# ============================================================
# Função principal do script
# Orquestra todas as etapas:
# 1) Conecta ao Firestore
# 2) Carrega o JSON
# 3) Envia os dados
# ============================================================
def main():
    print("Conectando ao Firestore...")
    db = conectar_firestore()

    print("Carregando arquivo JSON...")
    dados = carregar_json()

    print(f"Enviando {len(dados)} registros para o Firestore...")
    enviar_para_firestore(db, dados)

    print("✅ Importação concluída com sucesso!")


# ============================================================
# Ponto de entrada do script
# Garante que o main() só rode quando o arquivo for executado
# diretamente (e não importado)
# ============================================================
if __name__ == "__main__":
    main()
