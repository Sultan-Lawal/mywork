from sqlcommand import MySQLCommand

command = MySQLCommand()

options = [
    "\n<=== Welcome to Admin Control. ===>\n",
    "Choose an operation to perform: \n",
    "\t1. Connect Admin",
    "\t2. Create a new user",
    "\t3. Create database",
    "\t4. Grant privileges to user",
    "\t5. Exit\n"
]

commands = [
    command.connect_admin,
    command.create_user,
    command.create_database,
    command.grant_privileges,
    command.close_connection
]


def run_full_command():
    print("\n--- Running Full Automated Database Operations Wizard ---")
    for command in commands:
        command()

def run_partial_command():

    while True:
        for option in options:
            print(option)
        try:
            choice = int(input("Choose an option (1-5): "))

            print()

            # Connect Admin
            if choice == 1:
                print("Connect Admin Mode.\n")
                command.connect_admin()

            elif choice == 2:
                print("Create New User Mode.\n")
                command.create_user()

            elif choice == 3:
                print("Create Database Mode.\n")
                command.create_database()

            elif choice == 4:
                print("Grant Privileges Mode.\n")
                command.grant_privileges()

            elif choice == 5:
                print("Exiting...")
                command.load()
                command.close_connection()
                print("Exited.")
                break

            else:
                print("Wrong Input!")
                print("Choose from the following options (1-5)\n")

        except Exception as e:
            print(f"An error occured!")
            print(f"Error: {e}")



if __name__ == "__main__":
    print("\n======================================")
    print("1. Run full database operations.")
    print("2. Perform partial database operation.")
    print("======================================")

    try:
        main_choice = int(input("Enter a choice (1-2): "))
        print()

        if main_choice == 1:
            run_full_command()
        elif main_choice == 2:
            run_partial_command()
        else:
            print("\nInvalid Choice. Script terminated.\n")
    except ValueError:
        print("\nInvalid input. You must input a number (1 or 2).\n")