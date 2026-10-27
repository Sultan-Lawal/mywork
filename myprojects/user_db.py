import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "orderdb"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE orderdb")

sql = """CREATE TABLE orders (
  orderId INT NOT NULL AUTO_INCREMENT,
  userId INT NOT NULL,
  productId INT NOT NULL,
  size VARCHAR(50),
  quantity INT NOT NULL,
  price INT NOT NULL,
  orderDate TIMESTAMP NOT NULL,
  deliveryDate TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (orderId)
)"""

def add_order(userId, productId, size, quantity, price, orderDate, deliveryDate):
    sql = """ INSERT INTO 
    orders (userId, productId, size, quantity, price, orderDate, deliveryDate)
    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    
    order = (userId, productId, size, quantity, price, orderDate, deliveryDate)

    mycursor.execute(sql, order)
    mydb.commit()

def search_order(orderId):
    sql = "SELECT * FROM orders WHERE orderId = %s"
    order_id = (orderId,)

    mycursor.execute(sql, order_id)
    return mycursor.fetchone()  
       

def view_table():
    sql = "SELECT * FROM orders"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    

    for r in myresult:
        print(r)    

def order_exists(orderId):
    sql = "SELECT * FROM orders WHERE orderId = %s"
    order_id = (orderId,)

    mycursor.execute(sql, order_id)
    myresult = mycursor.fetchone()
    return myresult is not None


def update_order(orderId, userId, productId, size, quantity, price, orderDate, deliveryDate):
    sql = """UPDATE orders  
    SET userId = %s,
        productId = %s,
        size = %s,
        quantity = %s,
        price = %s,
        orderDate = %s,
        deliveryDate = %s
      WHERE orderId = %s"""

    order = (userId, productId, size, quantity, price, orderDate, deliveryDate, orderId)

    mycursor.execute(sql, order)
    mydb.commit()    
    return mycursor.rowcount > 0    

def delete_order(orderId):
    sql = "DELETE FROM orders WHERE orderId = %s"
    order = (orderId,)

    mycursor.execute(sql, order)
    mydb.commit()
    return mycursor.rowcount > 0