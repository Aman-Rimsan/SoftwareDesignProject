import csv  # Importing CSV module to handle CSV file operations

class ProductDatabase:
    
    #Class to manage product inventory stored in a CSV file.

    def __init__(self, filename="Estock.csv"): 

        '''constructor to initialize the class with the filename and products list'''
        #Initializes the ProductDatabase.
        #- filename: Name of the CSV file where product data is stored.
        #- products: List to store product data in memory.
        
        self.filename = filename
        self.products = []
        self.read_file()  # Load products from the file when initializing the class

    def read_file(self):
        
        #Reads product data from the CSV file and stores it in the `products` list.
        #If the file is missing, it creates a new one with sample data.
        

        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                # Store each product as a dictionary with lowercase names
                self.products = [{"name": row["name"].strip().lower(), 
                      
                '''The product name is converted to lowercase and stripped of any unnecessary spaces (row["name"].strip().lower()).
                The price is converted to a floating-point number (float(row["price"])).
                The stock quantity is converted to an integer (int(row["stock"])).'''

                                  "price": float(row["price"]), 
                                  "stock": int(row["stock"])} for row in reader]
            print("\nFile read successfully.")

        except FileNotFoundError:
            print("\nFile not found. Creating a new one with sample data.")
            self.create_sample_data()  # Calls a method (not included) to create default data
        except Exception as e:
            print(f"Error reading file: {e}")

    def write_file(self):
        
        #Writes the current product list back to the CSV file.
        
        try:
            with open(self.filename, mode='w', newline='') as file: # open the file in write mode and create a CSV writer object
                # Define the CSV column headers
                fieldnames = ["name", "price", "stock"]
                # These headers match the keys used in our product dictionary
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                # Write the header and data to the file
                writer.writeheader()  # Writing CSV column headers
                # Writing product data to the file
                writer.writerows(self.products)  # Writing product data to file
        except Exception as e:
            print(f"Error writing to file: {e}")

    def view_products(self):
        
        #Displays all products in the inventory in a tabular format.
        
        if not self.products:
            print("\nNo products available.") # If there are no products in the inventory, it displays a message and exits the method
            return
        print("\nInventory:") # Display the product inventory in a tabular format
        print(f"{'Name':<15} {'Price':<10} {'Stock':<10}")
        print("="*35) # Display a line of equal signs to separate the header from the product data
        for product in self.products:  
            print(f"{product['name']:<15} ${product['price']:<10.2f} {product['stock']:<10}") # Display each product's name, price, and stock in a formatted manner

    def add_product(self):
        
        #Adds a new product to the inventory.
        #Ensures product names are unique and that price and stock values are valid.
        
        name = input("Enter product name: ").strip().lower()
        if any(p['name'] == name for p in self.products):
            print("Product already exists.")  # Prevent duplicate product names
            return
        try:
            price = float(input("Enter product price: "))
            stock = int(input("Enter initial stock: "))
            if price < 0 or stock < 0:
                print("Stock and price must be non-negative.")
                return
        except ValueError:
            print("Invalid input. Price must be a number, stock must be an integer.")
            return
        
        self.products.append({"name": name, "price": price, "stock": stock})
        self.write_file()  # Save new product to the file
        print(f"Product '{name}' added successfully.")

    def edit_product(self):
        
        #Allows the user to modify the price and stock of an existing product.
        
        name = input("Enter product name to edit: ").strip().lower()
        for product in self.products:
            if product['name'] == name:
                try:
                    new_price = float(input(f"Enter new price for {name} (current: {product['price']}): "))
                    new_stock = int(input(f"Enter new stock for {name} (current: {product['stock']}): "))
                    if new_price < 0 or new_stock < 0:
                        print("Price and stock must be non-negative.")
                        return
                    product['price'] = new_price
                    product['stock'] = new_stock
                    self.write_file()  # Save updated product details to file
                    print(f"Product '{name}' updated successfully.")
                    return
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    return
        print(f"Product '{name}' not found.")  # If the product doesn't exist

    def search_products(self):
        
        #Searches for products containing a specific keyword.
        #Displays matching products if found.
        
        keyword = input("Enter product name or keyword to search: ").strip().lower()
        results = [p for p in self.products if keyword in p['name']]
        if results:
            print("\nSearch Results:")
            for product in results:
                print(f"{product['name']} - ${product['price']} - Stock: {product['stock']}")
        else:
            print("No matching products found.")

def main_menu():
    #Displays the main menu and allows the user to navigate different functionalities.
    db = ProductDatabase()  # Initialize the database instance
    while True:
        print("\nInventory Management System")
        print("1. View Products")
        print("2. Add Product")
        print("3. Edit Product")
        print("4. Search Products")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            db.view_products()  # View inventory
        elif choice == "2":
            db.add_product()  # Add new product
        elif choice == "3":
            db.edit_product()  # Edit existing product
        elif choice == "4":
            db.search_products()  # Search for products
        elif choice == "5":
            print("Exiting program.")  # Exit program
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

# Start the program
main_menu()
# The ProductDatabase validates the input to ensure it is correct. If the input is invalid, the user is prompted to enter the correct input. 
# The product data is then saved to the CSV file, and a confirmation message is displayed to the user.

'''
UML Class Diagram
+---------------------+
|  ProductDatabase    |
+---------------------+
| filename: str       |
| products: list      |
+---------------------+
| + __init__()        |
| + read_file()       | 
| + write_file()      |
| + view_products()   |
| + add_product()     |
| + edit_product()    |
| + search_products() |
+---------------------+


UML Sequence Diagram(add_product)

User          ProductDatabase
 |                  |
 |  Enters Product  |  
 |----------------->|
 |                  |
 |  Validates Input |  
 |----------------->|
 |  Saves to CSV    |  
 |----------------->|
 |  Confirmation    |  
 |<-----------------|

 User          ProductDatabase(edit_product)
 |                          |
 |  Selects Product to Edit |
 |------------------------> |
 |                          |
 |  Updates Price/Stock     |
 |------------------------->|
 |  Saves Changes to CSV    |
 |------------------------->|
 |  Confirmation            |
 |<-------------------------|

 User            ProductDatabase(Search_product)
 |                      |
 |  Enters Search Query |
 |--------------------->|
 |  Searches for Matches|
 |--------------------->|
 |  Displays Results    |
 |<---------------------|
'''

