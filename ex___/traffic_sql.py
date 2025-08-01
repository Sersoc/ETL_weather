import sqlite3, pandas as pd

conn = sqlite3.connect('traffic.db')
cursor = conn.cursor()

create_train_table_sql = """
CREATE TABLE train(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER,
    vector TEXT
);
"""

create_time_table_sql = """
CREATE TABLE time_table(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_id INTEGER,
    traffic_time DATETIME,
    FOREIGN KEY (train_id) REFERENCES train(id),
);
"""

insert_train_id = """
INSERT INTO train (number,vector) VALUES (?,?);
"""
select_train = """
SELECT * FROM train;
"""
def create_traffic_table():
    cursor.execute(create_train_table_sql)
    cursor.execute(create_time_table_sql)

def insert_train():
    
    cursor.execute(insert_train_id,(2,'상선'))
    conn.commit()
def show_traffic_table():
    df = pd.read_sql_query(select_train,conn)
    print(df)
    
    