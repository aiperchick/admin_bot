import sqlite3
from pathlib import Path


def creat_table():
    """
    функция для создание таблиц 'товары' и 'заказы' в БД
    """


DB_NAME = 'db_sqlite3'
DB_PATH = Path(__file__).parent.parent
global db, cur
db = sqlite3.connect(DB_PATH/DB_NAME)
cur = db.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS products(
product_id INTEGER PRIMARY KEY,
name TEXT,
price INTEGER
)""")

cur.execute(
    """CREATE TABLE IF NOT EXISTS products (
product_id INTEGER PRIMARY KEY,
name TEXT,
price INTEGER,
FOREIGN KEY (product_id)
    REFERENCES products (products_id)
    ON DELETE CASCADE
    )
""")

db.commit()


def populate_products():
    """
    заполняем таблицу
    """
    db.execute("""INSERT INTO products(
        name, price
    )
    VALUES ('шаурма 1', 200, './photo/arabskaja-shaurma.jpg'),
    ('hotdog', 150, './photo/arabskaja-shaurma.jpg'),
    ('coffee', 70, './photo/arabskaja-shaurma.jpg')
    """)
    db.commit()


def get_products():
    """
    Функция чтобы достать данные из таблицы по страницам
    """
    cur.execute("""
    SELECT * FROM products
    """)
    return cur.fetchall()


def order_process(data):
    """
    Фунцкия для заполнения order
    """
    data = data.as_dict()
    cur.execute("""INSERT INTO orders(
        username,
        address,
        day,
        product_id
    ) VALUES (:user_name,:address,:age,:day,:product_id)""",
                {'user_name': data['name'],
                 'address': data['address'],
                 'day': data['day'],
                 'product_id': data['product_id']})
    db.commit()


creat_table()
populate_products()
db.close()