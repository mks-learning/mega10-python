import psycopg2
    

def create_table():
    connection = psycopg2.connect("dbname='first_table' user='postgres' password='P@ssw0rd' host = 'localhost' port='5432'")
    cursorobj = connection.cursor()
    cursorobj.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname='first_table' user='postgres' password='P@ssw0rd' host = 'localhost' port='5432'")
    cursorobj = connection.cursor()
    cursorobj.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = psycopg2.connect("dbname='first_table' user='postgres' password='P@ssw0rd' host = 'localhost' port='5432'")
    cursorobj = connection.cursor()
    cursorobj.execute("SELECT * FROM store")
    rows = cursorobj.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = psycopg2.connect("dbname='first_table' user='postgres' password='P@ssw0rd' host = 'localhost' port='5432'")
    cursorobj = connection.cursor()
    cursorobj.execute("DELETE FROM store WHERE item=%s",(item,))
    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = psycopg2.connect("dbname='first_table' user='postgres' password='P@ssw0rd' host = 'localhost' port='5432'")
    cursorobj = connection.cursor()
    cursorobj.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    connection.commit()
    connection.close()

# create_table()
update(24,1.99,'Orange')
print(view())
# update(11,6,"Water Glass")
# # delete("Wine Glass")
# print(view())