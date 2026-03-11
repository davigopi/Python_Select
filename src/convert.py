from var import *
from bs4 import BeautifulSoup
import json
import csv
import time

class Convert:
    def __init__(self, *args, **kwargs):
        self.table = kwargs.get('table')
        self.disc = kwargs.get('disc')
        self.json = kwargs.get('json')


    def table_html_in_disc(self):
        if not self.table:
            return []
        header_row = self.table.find(tag_tr)
        headers = [th.get_text(strip=True).replace("\n", " ") for th in header_row.find_all(tag_th)]
        rows = []
        for tr in self.table.find_all(tag_tr)[1:]:
            cells = [td.get_text(strip=True).replace("\n", " ") for td in tr.find_all(tag_td)]
            if cells: 
                rows.append(dict(zip(headers, cells)))
        return rows

    def table_list_in_disc(self):
        if not self.table:
            return []
        headers = self.table[0]
        return [dict(zip(headers, linha)) for linha in self.table[1:]]
    
    def disc_in_json(self):
        if not self.disc:
            return json.dumps([], indent=4, ensure_ascii=False)
        return json.dumps(self.disc, indent=4, ensure_ascii=False)
    
    def json_in_disc(self):
        if not self.json:
            return {}
        return json.loads(self.json)





if __name__ == '__main__':
    import main
    # main()

