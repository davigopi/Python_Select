# flake8: noqa
# pyright: # type: ignore

import os
import sys
import json
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.utils import ensure_folder

# def full_path(path_file):
#     if getattr(sys, 'frozen', False):
#         # Quando for .EXE do PyInstaller
#         base = os.path.dirname(sys.executable)
#     else:
#         # Quando rodar como .py (pega o local do main)
#         # base = os.path.dirname(os.path.abspath(sys.argv[0]))
#         base = os.path.dirname(os.path.abspath(__file__))
#     full_folder_file = os.path.normpath(os.path.join(base, path_file))
#     ensure_folder(full_folder_file)
#     return full_folder_file
def full_path(path_file):
    if getattr(sys, 'frozen', False):
        base = Path(sys.executable).parent
    else:
        base = Path(__file__).resolve().parent.parent  # sobe 1 nível

    full_folder_file = base / path_file
    full_folder_file.parent.mkdir(parents=True, exist_ok=True)
    # full_folder_file.mkdir(parents=True, exist_ok=True)

    return str(full_folder_file)


class Read_salve:
    def __init__(self, *args, **kwargs):
        self.write_file = kwargs.get('write_file')
        self.path_file = kwargs.get('path_file')

    def to_read(self):
        full_folder_file = full_path(self.path_file)
        ext = os.path.splitext(str(self.path_file))[1].lower()
        mode = "r"
        encoding = "utf-8"
        # print(full_folder_file)
        with open(full_folder_file, mode, encoding=encoding) as arq:
            if ext == ".json":
                return json.load(arq)
            elif ext == ".txt":
                return arq.read()
            elif ext == ".csv":
                reader = csv.reader(arq)
                return list(reader)
            else:
                raise ValueError(f"Extensão não suportada: {ext}")

    def to_write(self):
        full_folder_file = full_path(self.path_file)
        ext = os.path.splitext(str(self.path_file))[1].lower()
        mode = "w"  # ou "a", depende do que você quer
        encoding = "utf-8"
        try:
            with open(full_folder_file, mode, encoding=encoding) as arq:
                if ext == ".json":
                    # self.write_file = json.dumps(self.write_file, ensure_ascii=False, indent=4)
                    # print(f'self.write_file: {self.write_file}')
                    json.dump(self.write_file, arq, ensure_ascii=False, indent=4)
                elif ext == ".txt":
                    arq.write(str(self.write_file) + "\n")
                elif ext == ".csv":
                    if isinstance(self.write_file, (list, tuple)):
                        arq.write(",".join(map(str, self.write_file)) + "\n")
                    else:
                        arq.write(str(self.write_file) + "\n")
                else:
                    raise ValueError(f"Extensão não suportada: {ext}")
        except Exception as e:
            print(f"Erro ao salvar: {e}")


    def to_clean(self):
        full_folder_file = full_path(self.path_file)
        mode = "w"  # ou "a", depende do que você quer
        encoding = "utf-8"
        # Garante que o arq exista antes de limpar
        if os.path.exists(full_folder_file):
            with open(full_folder_file, mode, encoding=encoding) as arq:
                arq.write('')
            return True
        else:
            return False

    def to_delete(self):
        full_folder_file = full_path(self.path_file)

        if os.path.exists(full_folder_file):
            os.remove(full_folder_file)
            return True
        else:
            return False