import psycopg2

class PostgresDB:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

        self.connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
        )

        self.cursor = self.connection.cursor()
        self.connection.autocommit = True
    
    def ensure_table(self, ddl_file):
        with open(ddl_file, "r", encoding="utf-8") as f:
            ddl = f.read()
            self.cursor.execute(ddl)
    
    def insert_rows(self, table_name, rows):
        if not rows:
            return
        
        columns = rows[0].keys()
        columns_str = ", ".join(columns)

        placeholders = ", ".join(["%s"] * len(rows[0]))

        sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});"
        values = [tuple(row.values()) for row in rows]
        self.cursor.executemany(sql, values)

    def close(self):
        if self.connection:
            self.connection.close()