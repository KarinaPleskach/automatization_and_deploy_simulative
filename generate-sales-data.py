import os
import ast
import configparser
import random
import string
import csv

# load config file
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "config.ini"), encoding="utf-8")

# make data dir
data_dir = os.path.join(os.getcwd(), config["Dirs"]["DATA_DIR"])
os.makedirs(data_dir, exist_ok=True)

# load categories
categories = {}
for key, value in config["Categories"].items():
    categories[key] = ast.literal_eval(value)

# generate doc_id
def random_doc_id(n=10):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))

# generate one data file
def generate_csv(shop_num, cash_num, receipts_count=None):
    if receipts_count is None:
        receipts_count = random.randint(3, 10)

    rows = []
    for _ in range(receipts_count):
        doc = random_doc_id()
        # each receipt has 1..4 items
        for _ in range(random.randint(1,4)):
            category = random.choice(list(categories.keys()))
            item = random.choice(categories[category])
            amount = random.randint(1, 10)
            price = round(random.uniform(1.5, 120.0), 2)
            # in 60% of time discount will be 0
            discount = 0.0 if random.random() < 0.6 else round((price) * random.choice([0.05, 0.1, 0.15]), 2)
            rows.append({
                "doc_id": doc,
                "item": item,
                "category": category,
                "amount": amount,
                "price": price,
                "discount": discount
            })

    filename = os.path.join(data_dir, f"{shop_num}_{cash_num}.csv")
    with open(filename, "w", newline="", encoding="utf-8") as f:
        columns = ["doc_id", "item", "category", "amount", "price", "discount"]
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

# generate several csv files
for shop in range(1, 4):
    for cash in range(1, 3):
        generate_csv(shop, cash)
