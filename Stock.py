import csv  # Importing CSV module to handle CSV file operations

class ProductDatabase:
    
    #Class to manage product inventory stored in a CSV file.

    def __init__(self, filename="Estock.csv"):
        self.filename = filename 
        self.products = []
        self.read_file()  # Load products from the file when initializing the class

    def read_file(self):
        try:
            with open(self.filename, mode='r', newline='') as file:     # Open the file in read mode
                reader = csv.DictReader(file)                           # Create a CSV DictReader object
                self.products = [{"name": row["name"].strip().lower(),  # Read each row as a dictionary and append it to the products list
                                  "price": float(row["price"]),         # Convert price to float
                                  "stock": int(row["stock"])} for row in reader]   # Convert stock to integer
            print("\nFile read successfully.")
        except FileNotFoundError:
            print("\nFile not found. Creating a new one with sample data.")
            self.create_sample_data()
        except Exception as e:
            print(f"Error reading file: {e}")

    def write_file(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                # Open the file in write mode, create a CSV DictWriter object, 
                # write the header, and write the products list to the file.
                # The fieldnames are the keys of the first product in the list.
                fieldnames = ["name", "price", "stock"]
                writer = csv.DictWriter(file, fieldnames=fieldnames) 
                writer.writeheader() 
                writer.writerows(self.products) 
        except Exception as e:
            print(f"Error writing to file: {e}")

    def view_products(self):
        if not self.products:                                 # If there are no products in the list, print a message and return.
            print("\nNo products available.")  
            return
        print("\nInventory:")
        print(f"{'Name':<15} {'Price':<10} {'Stock':<10}")    # Print the header, then loop through the products and print each one.
        print("="*35) 
        for product in self.products:
            print(f"{product['name']:<15} ${product['price']:<10.2f} {product['stock']:<10}")

    def add_product(self):
        name = input("Enter product name: ").strip().lower()
        if any(p['name'] == name for p in self.products):
            print("Product already exists.")
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
        self.write_file()
        print(f"Product '{name}' added successfully.")

    def edit_product(self):
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
                    self.write_file()
                    print(f"Product '{name}' updated successfully.")
                    return
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    return
        print(f"Product '{name}' not found.")

    def search_products(self):
        keyword = input("Enter product name or keyword to search: ").strip().lower()
        results = [p for p in self.products if keyword in p['name']]
        if results:
            print("\nSearch Results:")
            for product in results:
                print(f"{product['name']} - ${product['price']} - Stock: {product['stock']}")
        else:
            print("No matching products found.")

    def filter_products(self):  # filters all products based on the stock range and sorts them alphabetically if required.
        order = input("Sort alphabetically? (y/n): ").strip().lower() # Ask the user if they want to sort the results alphabetically, then get the minimum and maximum stock values.
        min_stock = input("Enter minimum stock (leave blank for no limit): ").strip()  
        max_stock = input("Enter maximum stock (leave blank for no limit): ").strip() 
        
        try:
            min_stock = int(min_stock) if min_stock else 0 
            '''If min_stock is not provided, set it to 0.
            If min_stock is provided, convert it to an integer.
            '''
            max_stock = int(max_stock) if max_stock else float('inf') 

        except ValueError:
            print("Invalid stock range values.")
            return
        
        filtered = [p for p in self.products if min_stock <= p['stock'] <= max_stock]
        if order == 'y':
            filtered.sort(key=lambda x: x['name'])
        
        if not filtered:
            print("\nNo matching products found.")
            return # If no products match the filter criteria, print a message and return.
        print("\nInventory:")
        print(f"{'Name':<15} {'Price':<10} {'Stock':<10}") # Print the header, then loop through the filtered products and print each one.
        print("="*35)
        for product in filtered:
            print(f"{product['name']:<15} ${product['price']:<10.2f} {product['stock']:<10}")


def main_menu():
    db = ProductDatabase()
    while True:
        print("\nInventory Management System")
        print("1. View Products")
        print("2. Product")
        print("3. Edit Product")
        print("4. Search Products")
        print("5. Filter Products")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            db.view_products()
        elif choice == "2":
            db.add_product()
        elif choice == "3":
            db.edit_product()
        elif choice == "4":
            db.search_products()
        elif choice == "5":
            db.filter_products()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main_menu()

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
