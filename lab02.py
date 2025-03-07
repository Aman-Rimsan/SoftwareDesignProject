import csv

class ProductDatabase:
    def __init__(self, filename="Estock.csv"):
        # Initialize the database with a filename and read existing data
        self.filename = filename
        self.products = []
        self.read_file()
    
    def read_file(self):
        # Read product data from the CSV file
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.products = [{"name": row["name"].strip().lower(), 
                                  "price": float(row["price"]), 
                                  "stock": int(row["stock"])} for row in reader]
            print("\nFile read successfully.")
        except FileNotFoundError:
            print("\nFile not found. Creating a new one with sample data.")
            self.create_sample_data()
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def write_file(self):
        # Write product data back to the CSV file
        try:
            with open(self.filename, mode='w', newline='') as file:
                fieldnames = ["name", "price", "stock"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.products)
        except Exception as e:
            print(f"Error writing to file: {e}")
    
    def view_products(self):
        # Display all products in the inventory
        if not self.products:
            print("\nNo products available.")
            return
        print("\nInventory:")
        print(f"{'Name':<15} {'Price':<10} {'Stock':<10}")
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
        # Edit an existing product in the inventory
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
        # Search for products by name or keyword
        #This function allows users to search for a product in the inventory using a keyword.
        #It checks if the keyword exists in any product name and displays matching results.
        keyword = input("Enter product name or keyword to search: ").strip().lower()
        results = [p for p in self.products if keyword in p['name']]
        if results:
            print("\nSearch Results:")
            for product in results:
                print(f"{product['name']} - ${product['price']} - Stock: {product['stock']}")
        else:
            print("No matching products found.")

def main_menu():
    # Main menu loop for user interaction
    db = ProductDatabase()
    while True:
        print("\nInventory Management System")
        print("1. View Products")
        print("2. Add Product")
        print("3. Edit Product")
        print("4. Search Products")
        print("5. Exit")
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
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
