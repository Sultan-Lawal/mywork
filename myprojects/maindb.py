import mysql.connector as con

# Connect the super admin
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password"
}

conn = con.connect(**db_config)
cursor = conn.cursor()
print("Connected")


cmd = cursor.execute("show databases")
print(cmd)

class Admin:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect_admin(self, host, user, password):
        auth_params = {
            "host": host,
            "user": user,
            "password": password
        }

        self.conn = con.connect(**auth_params)
        self.cursor = self.conn.cursor()
        print("Connected")


    def create_user(self, host, user, password):
        if not self.conn:
            print("No active server connection. Connect admin account first.")

            print()
        
        else:
            try:
                cmd = F"CREATE USER '{user}'@'{host}' IDENTIFIED BY '{password}';"
                self.cursor.execute(cmd)

                print("User created")

            except Exception as e:
                print(f"Error creating user: {e}")
                print("Check if user already exists.")

    
    def create_db(self, db_name):
        try:
            cmd = f" CREATE DATABASE {db_name}; "
            self.cursor.execute(cmd)

            print("Database Created")

        except Exception as e:
            print(f"Error creating database: {e}")
            print("Check if database already exists.")


    def grant_user_privileges(self, db_name, user, host, privileges="ALL"):
        try:
            cmd = f" GRANT {privileges} PRIVILEGES ON `{db_name}`.* TO '{user}'@'{host}';"
            flush = " FLUSH PRIVILEGES; "
            self.cursor.execute(cmd)
            self.cursor.execute(flush)

            print("Granted")
        
        except Exception as e:
            print(f"Error granting privilege: {e}")


    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

        print("Connection close successfully")


admin = Admin()

admin.connect_admin("localhost", "root", "Olamide@1")
admin.create_user("localhost", "new", "password")
admin.create_db("students")
admin.grant_user_privileges("students", "new", "localhost")
admin.close_connection()


def create_table(host, user, password, db, table_name):
    # First connect user to db
    auth_params = {
        "host": host,
        "user": user,
        "password": password,
        "database": db
    }

    conn = con.connect(**auth_params)
    cursor = conn.cursor()

    try:
        cmd = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
            orderId INT AUTO_INCREMENT PRIMARY KEY,
            userId INT,
            productId INT,
            size VARCHAR(50), 
            quantity INT, 
            price INT, 
            orderDate TIMESTAMP, 
            deliveryDate TIMESTAMP
            );
            """
        cursor.execute(cmd)
        conn.commit()
        print(f"Table {table_name} created")

    except Exception as e:
        print(f"Error creating table: {e}")

    finally:
        cursor.close()
        conn.close()


table = create_table("localhost", "new", "password", "students", "orders")


"""
orderId int not null primary key, 
userId int, 
productId int, 
size varchar(50), 
quantity int, 
price int, 
orderDate TIMESTAMP, 
deliveryDate TIMESTAMP 
"""