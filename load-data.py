import os
import configparser

from db import PostgresDB
from loader import CSVLoader

# read config.ini
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "config.ini"), encoding="utf-8")

ddl_file = os.path.join(os.getcwd(), config["Dirs"]["DDL_DIR"])
data_dir = os.path.join(os.getcwd(), config["Dirs"]["DATA_DIR"])
table_name = config["Database"]["TABLE"]
db_params = config["Database"]

#connect to db
db = PostgresDB(
    host=db_params["HOST"],
    database=db_params["DATABASE"],
    user=db_params["USER"],
    password=db_params["PASSWORD"],
)
db.ensure_table(ddl_file)

#load data
loader = CSVLoader(db, data_dir)
loader.load_csv_files(table_name="sales")

db.close()