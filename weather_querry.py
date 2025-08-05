import sqlite3
import weather_sql as sql

conn = sqlite3.connect('weather.db')
conn.execute('PRAGMA foreign_keys = ON')

cursor = conn.cursor()
def create_tables():
    cursor.execute(sql.create_table_location)
    cursor.execute(sql.create_table_logging_time)
    cursor.execute(sql.create_table_rain)
    cursor.execute(sql.create_table_temp)
    cursor.execute(sql.create_table_wind)

def insert_data_to_db(data):
    data