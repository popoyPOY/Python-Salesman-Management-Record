import sqlite3


def salesman():

    conn = sqlite3.connect('SalesFile.db')

    conn.execute('''
        CREATE TABLE salesman (salesman_no INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                              salesman_number INT,
                              salesman_name TEXT,
                              salesman_gender TEXT,
                              salesman_age TEXT,
                              salesman_address TEXT)
    ''')

    conn.commit()
    conn.close()

salesman()

def sales():
    
    conn = sqlite3.connect('SalesFile.db')

    conn.execute('''
        CREATE TABLE sales (salesman_number TEXT,
                            sales_name TEXT,
                            sales_stock INT,
                            sales_quantity INT,
                            sales_unit TEXT,
                            sales_description TEXT,
                            sales_price REAL,
                            sales_amount REAL,
                            sales_commission REAL,
                            sales_net_amount REAL)
    ''')

    conn.commit()
    conn.close()

sales()