import time
import mysql.connector as con


class MySQLCommand:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.db_name = None
        self.new_username = None
        self.new_user_host = None
        self.terminate = ["exit", "quit"]
        self.prompt_value = ["y", "yes", "Y", "Yes"]


    def load(self):
        for i in range(1, 4):
            time.sleep(1)
            print(i, end=", ", flush=True)
        print("4.")

    def should_terminate(self, user_input):
        if user_input.lower().strip() in self.terminate:
            prompt = input("Are you sure you want to terminate? (y/n): ")
            if prompt.lower().strip() in self.prompt_value:
                print("Terminating...")
                self.load()
                print("Terminated successfully.")
                return True
            else:
                return
        return False
            

    def docs(self):
        docs = """
        --------------------------------------------------------
        |    Note: Input matching relies on exact string cases.|
        |                                                      |
        |    Enter exit/quit to terminate                      |
        --------------------------------------------------------
            """
        print(docs)


    def connect_admin(self):
        self.docs()
        
        while True:
            user = input("Enter the user name (e.g. root): ")
            if self.should_terminate(user): return
                
            host = input("Enter the host (e.g. localhost): ")
            if self.should_terminate(host): return
                
            password = input("Enter password: ")
            if self.should_terminate(password): return

            try:
                print("Connecting....")
                self.conn = con.connect(
                    host=host,
                    user=user,
                    password=password
                )
            
                self.cursor = self.conn.cursor()
                self.load()
                print("Successfully connected to MySQL Database Server!")
                break

            except Exception as e:
                print(f"Connection failed: {e}. Please try again")
                break
            

    def create_user(self):
        self.docs()
        if not self.conn:
            print("No active server connection. Connect admin account first.")
            self.connect_admin()
            if not self.conn: return

            print()

        while True:
            name = input("Enter new user name: ")
            if self.should_terminate(name): return
                
            host = input("Enter the host (e.g. localhost): ")
            if self.should_terminate(host): return

            password = input("Enter new user password: ")
            if self.should_terminate(password): return


            cmd = f"""
            CREATE USER '{name}'@'{host}' IDENTIFIED BY '{password}';
            """

            try:
                print(f"Creating user '{name}'...")
                self.cursor.execute(cmd)

                self.new_username = name
                self.new_user_host = host

                self.load()
                print("Successfully created user to MySQL Database Server!")
                break

            except Exception as e:
                print(f"Connection failed: {e}")
                break


    def create_database(self):
        if not self.conn:
            print("No active server connection. Connect admin account first.")
            self.connect_admin()
            if not self.conn: return
        self.docs()
        

        while True:
            db_name = input("Enter new database name: ")
            if self.should_terminate(db_name): return

            cmd = f" CREATE DATABASE {db_name}; "

            try:
                print(f"Creating database '{db_name}'...")
                self.cursor.execute(cmd)
                self.db_name = db_name

                self.load()
                print("Successfully created database to MySQL Database Server!")
                break

            except Exception as e:
                print(f"Connection failed: {e}")
                break



    def grant_privileges(self):
        if not self.conn:
            print("No active server connection. Initializing Admin Connection...")
            self.connect_admin()
            if not self.conn: return

        username = self.new_username
        user_host = self.new_user_host
        user_db_name = self.db_name

        if not username:
            username = input("Enter username: ")
            if self.should_terminate(username): return

        if not user_host:
            user_host = input("Enter user host: ")
            if self.should_terminate(user_host): return

        if not user_db_name:
            user_db_name = input("Enter database name: ")
            # Fixed Indentation Error
            if self.should_terminate(user_db_name): return

        while True:
            cmd = f" GRANT ALL PRIVILEGES ON `{user_db_name}`.* TO '{username}'@'{user_host}';" 
            flush = " FLUSH PRIVILEGES; "

            try:
                print(f"Granting privileges on {user_db_name} to {username}...")
                self.cursor.execute(cmd)
                self.cursor.execute(flush)

                self.load()
                print("Successfully granted user all privileges!")
                break
            except Exception as e:
                print(f"Connection failed: {e}")
                break

    def close_connection(self):
        """Clean resources management"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()