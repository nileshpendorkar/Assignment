import sqlite3 
import threading 

# Databases  
USERS_DB = 'users.db' 
ORDERS_DB = 'orders.db' 
PRODUCTS_DB = 'products.db' 

# data 

users_data = [ 
(1, 'Alice', 'alice@example.com'), 
(2, 'Bob', 'bob@example.com'), 
(3, 'Charlie', 'charlie@example.com'), 
(4, 'David', 'david@example.com'), 
(5, 'Eve', 'eve@example.com'), 
(6, 'Frank', 'frank@example.com'), 
(7, 'Grace', 'grace@example.com'), 
(8, 'Alice', 'alice@example.com'), 
(9, 'Henry', 'henry@example.com'), 
(10, 'Jane', 'jane@example.com')
]

products_data = [ 
    (1, 'Laptop', 1000.00), 
    (2, 'Smartphone', 700.00), 
    (3, 'Headphones', 150.00), 
    (4, 'Monitor', 300.00), 
    (5, 'Keyboard', 50.00), 
    (6, 'Mouse', 30.00), 
    (7, 'Laptop', 1000.00), 
    (8, 'Smartwatch', 250.00), 
    (9, 'Gaming Chair', 500.00), 
    (10, 'Earbuds', 50.00) 
    ] 

orders_data = [ 
    (1, 1, 1, 2), 
    (2, 2, 2, 1), 
    (3, 3, 3, 5), 
    (4, 4, 4, 1), 
    (5, 5, 5, 1), 
    (6, 6, 6, 7), 
    (7, 7, 7, 8), 
    (8, 8, 8, 9), 
    (9, 9, 9, 10), 
    (10, 10, 10, 11)
]

# tables 
def create_tables(): 
    conn = sqlite3.connect(USERS_DB) 
    c = conn.cursor() 
    c.execute('''CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''') 
    conn.commit()
    print(f"{users_data} \n Users data inserted successfully") 
    conn.close() 

    conn = sqlite3.connect(PRODUCTS_DB) 
    c = conn.cursor() 
    c.execute('''CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, name TEXT, price REAL)''') 
    conn.commit() 
    print(f"{products_data} \n Products data inserted successfully")
    conn.close() 

    conn = sqlite3.connect(ORDERS_DB) 
    c = conn.cursor() 
    c.execute('''CREATE TABLE IF NOT EXISTS Orders (id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER, quantity INTEGER)''') 
    conn.commit()
    print(f"{orders_data} \n Orders data inserted successfully")
    conn.close() 
    
# Insert data 
def insert_data(db, query, data): 
    conn = sqlite3.connect(db) 
    c = conn.cursor() 
    c.executemany(query, data) 
    conn.commit() 
    conn.close()

# Insert operations 
def insert_users(): 
    query = '''INSERT INTO Users (id, name, email) VALUES (?, ?, ?)''' 
    insert_data(USERS_DB, query, users_data) 
def insert_products(): 
    query = '''INSERT INTO Products (id, name, price) VALUES (?, ?, ?)''' 
    insert_data(PRODUCTS_DB, query, products_data) 
def insert_orders(): 
    query = '''INSERT INTO Orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)''' 
    insert_data(ORDERS_DB, query, orders_data)

# function to run insert operations concurrently 
def main(): 
    create_tables() 
    threads = [] 
    threads.append(threading.Thread(target=insert_users)) 
    threads.append(threading.Thread(target=insert_products)) 
    threads.append(threading.Thread(target=insert_orders)) 
    for thread in threads: 
        thread.start() 
    for thread in threads: thread.join() 
    print("Data inserted successfully!") 

if __name__ == '__main__': 
    main()