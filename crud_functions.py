import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE  IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER
    )
    ''')

def get_all_products():
    cursor.execute('''
    SELECT * FROM Products 
    ''')

    all_products = cursor.fetchall()

    return all_products

