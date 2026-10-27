import user_db

class Order:
    def __init__(self, userId, productId, size, quantity, price, orderDate, deliveryDate, orderId=None):
        self.user_id = userId
        self.product_id = productId
        self.size = size
        self.quantity = quantity
        self.price = price
        self.order_date = orderDate
        self.delivery_date = deliveryDate


    def display_info(self):
        # print(f"\nOrder ID: {self.orderId}")
        print(f"\nUser ID: {self.user_id}")
        print(f"Product Name: {self.product_id}") 
        print(f"Size: {self.size}") 
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")
        print(f"orderDate: {self.order_date}")
        print(f"deliveryDate: {self.delivery_date}")





class OrderManagement:
    def __init__(self):
        pass

    def view_order(self):    
        user_db.view_table()


    def add_order(self):
        while True:
           userId = int(input("Enter user ID (e.g. 1001 ): "))
           if userId >= 1001:
               break
           print("Invalid User ID! \nPlease enter a valid ID starting from 1001.")
        while True:   
           productId = int(input("Enter product ID (e.g. 5001): "))
           if productId >= 5001:
               break
           print("Invalid Product ID! \nPlease enter a valid ID starting from 5001.")

        size = input("Enter size: ").upper()
        quantity = int(input("Enter quantity: "))
        price = int(input("Enter price: "))
        orderDate = input("Enter order date&time (YYYY-MM-DD HH:MM:SS): ")
        deliveryDate = input("Enter delivery date&time (YYYY-MM-DD HH:MM:SS): ")
        




        user_db.add_order(userId, productId, size, quantity, price, orderDate, deliveryDate)

        print("\nOrder added successfully!")
    


    def remove_order(self):
        remove_id = int(input("Enter the order ID to remove: "))

        found = user_db.delete_order(remove_id)
                
        if found:        
            print("\nOrder removed successfully!")
        else:
            print("\nOrder ID not found!")    
        
    
    def update_order(self):
        update_orderId = int(input("Enter order ID to update: "))
        
        check = user_db.order_exists(update_orderId)
        if not check:
            print("\nOrder ID not found!")
            return

        # Collect the new information
        while True:
            new_userId = int(input("\nEnter new user ID (e.g. 1001): "))
            if new_userId >= 1001:
                break
            print("Invalid User ID! \nPlease enter a valid ID starting from 1001.")
        while True:    
            new_productId = int(input("Enter new product ID (e.g. 5001): "))
            if new_productId >= 5001:
                break
            print("Invalid Product ID! \nPlease enter a valid ID starting from 5001.")
        new_size = (input("Enter new size: ")).upper()
        new_quantity = int(input("Enter new quantity: "))
        new_price = int(input("Enter new price: "))
        new_orderDate = input("Enter new order date&time (YYYY-MM-DD HH:MM:SS): ")
        new_deliveryDate = input("Enter new delivery date&time (YYYY-MM-DD HH:MM:SS): ")

        success = user_db.update_order(update_orderId, new_userId, new_productId, new_size, new_quantity, new_price, new_orderDate, new_deliveryDate)

        if success:    
            print("\nOrder updated successfully!")


    def search_order(self):
        search_id = int(input("Enter order ID: "))
        found = user_db.search_order(search_id)
        if found:
            print(found)
        else:
            print("\nOrder ID not found!") 

           

    def option(self):
       while True:

        print("1. Create Order")
        print("2. Search Order by ID")
        print("3. Remove Order")
        print("4. Update Order")
        print("5. View Order")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            self.add_order()

        elif choice == "2":
            self.search_order()

        elif choice == "3":
            self.remove_order()

        elif choice == "4":
            self.update_order()

        elif choice == "5":
            self.view_order()

        elif choice == "6":
            print("Exiting....")
            break

        else:
            print("Invalid choice. Please try again!")
    



st1 = OrderManagement()
st1.option()


