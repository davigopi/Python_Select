from var import *
from bs4 import BeautifulSoup
import json
import csv
import time

class Convert:
    def __init__(self, *args, **kwargs):
        self.html_table = kwargs.get('html_table')


    def table_html_in_json(self):
        # print("TIPO:", type(self.html_table))
        # print(f'self.html_table: {self.html_table}')
        # soup = BeautifulSoup(str(self.html_table), "html.parser")

        # Pega a tabela
        # table = soup.find(tag_table)

        # Linha com cabeçalhos
        header_row = self.html_table.find(tag_tr)
        headers = [th.get_text(strip=True).replace("\n", " ") for th in header_row.find_all(tag_th)]

        # Linhas de dados
        rows = []
        for tr in self.html_table.find_all(tag_tr)[1:]:  # ignora cabeçalhos
            cells = [td.get_text(strip=True).replace("\n", " ") for td in tr.find_all(tag_td)]
            if cells:  # ignora linhas vazias
                rows.append(dict(zip(headers, cells)))

        print("JSON:")
        print(json.dumps(rows, ensure_ascii=False, indent=4))
        return rows


        # # Salvar CSV
        # with open("tabela.csv", "w", newline="", encoding="utf-8") as f:
        #     writer = csv.DictWriter(f, fieldnames=headers)
        #     writer.writeheader()
        #     writer.writerows(rows)

if __name__ == '__main__':
    import main
    # main()

