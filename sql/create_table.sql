CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    doc_id VARCHAR(20) NOT NULL,
    shop_num INTEGER NOT NULL,
    cash_num INTEGER NOT NULL,
    item VARCHAR(40) NOT NULL,
    category VARCHAR(40) NOT NULL,
    amount INTEGER,
    price NUMERIC(10,2),
    discount NUMERIC(10,2)
);