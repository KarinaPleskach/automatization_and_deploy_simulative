import os
import re
import pandas as pd

class CSVLoader:

    def __init__(self, db, data_dir):
        self.db = db
        self.data_dir = data_dir

    def load_csv_files(self, table_name):
        FILENAME_RE = re.compile(r"^\d+_\d+\.csv$")

        for file in os.listdir(self.data_dir):
            if not FILENAME_RE.match(file):
                print("Ignore file:", file)
                continue
            

            filepath = os.path.join(self.data_dir, file)
            rows = []
            shop_num, cash_num = map(int, file.replace(".csv","").split("_"))

            df = pd.read_csv(filepath)
            for i, row in df.iterrows():
                rows.append({
                    "doc_id": row["doc_id"],
                    "shop_num": shop_num,
                    "cash_num": cash_num,
                    "item": row["item"],
                    "category": row["category"],
                    "amount": row["amount"],
                    "price": row["price"],
                    "discount": row["discount"]
                })

            self.db.insert_rows(table_name, rows)
            os.remove(filepath)
