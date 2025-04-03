"""
Inventory Management System - Console Version
This script provides a command-line interface for managing product inventory.
Features include viewing, adding, editing, searching, sorting products, and role-based access control.
"""

import csv

class ProductDatabase:
    """
    Handles all product data operations including:
    - Reading/writing to CSV file
    - CRUD operations for products
    - Searching/sorting/filtering products
    - User authentication
    """
    
    def __init__(self, filename="Estock.csv"):
        """Initialize the database with specified CSV file."""
        self.filename = filename  # CSV file for product storage
        self.products = []        # List to store product dictionaries
        self.read_file()          # Load existing data on initialization

    def read_file(self):
        """Read product data from CSV file into memory."""
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                # Create product dictionaries with normalized data
                self.products = [{
                    "name": row["name"].strip().lower(),
                    "price": float(row["price"]),
                    "stock": int(row["stock"]),
                    "category": row["category"].strip().lower()
                } for row in reader]
        except FileNotFoundError:
            print("File not found. Creating a new one.")
            self.write_file()  # Create file if it doesn't exist
        except Exception as e:
            print(f"Error reading file: {e}")

    def write_file(self):
        """Write current product data to CSV file."""
        try:
            with open(self.filename, mode='w', newline='') as file:
                fieldnames = ["name", "price", "stock", "category"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.products)
        except Exception as e:
            print(f"Error writing to file: {e}")

    def view_products(self):
        """Display all products in a formatted table."""
        if not self.products:
            print("\nNo products available.")
            return

        # Calculate dynamic column widths based on content
        name_width = max(len(p["name"]) for p in self.products) + 2
        price_width = 10
        stock_width = 10
        category_width = max(len(p["category"]) for p in self.products) + 2

        # Print table header
        print("\nInventory:")
        print(f"{'Name'.ljust(name_width)} {'Price ($)'.ljust(price_width)} {'Stock'.ljust(stock_width)} {'Category'.ljust(category_width)}")
        print("=" * (name_width + price_width + stock_width + category_width))

        # Print each product's details
        for product in self.products:
            name = product['name'].title()  # Proper capitalization
            price = f"${product['price']:.2f}"  # Format as currency
            stock = str(product['stock'])
            category = product['category'].title()
            print(f"{name.ljust(name_width)} {price.ljust(price_width)} {stock.ljust(stock_width)} {category.ljust(category_width)}")

        print(f"\nTotal Products: {len(self.products)}")

    def add_product(self, name=None, price=None, stock=None, category=None):
        """Add a new product to the database."""
        if None in (name, price, stock, category):  # Interactive mode
            category = input("Enter product category (e.g., GPU, CPU, RAM, etc.): ").strip().lower()
            name = input("Enter product name: ").strip().lower()
            price = input("Enter product price: ")
            stock = input("Enter initial stock: ")
            
        if any(p['name'] == name for p in self.products):
            return "Product already exists."
            
        try:
            price = float(price)
            stock = int(stock)
            if price < 0 or stock < 0:
                return "Stock and price must be non-negative."
        except ValueError:
            return "Invalid input. Price must be a number, stock must be an integer."
            
        self.products.append({
            "name": name, 
            "price": price, 
            "stock": stock, 
            "category": category
        })
        self.write_file()
        return f"Product '{name}' added successfully."

    def search_products(self, search_term):
        """Search for products by name (case-insensitive partial match)."""
        search_term = search_term.strip().lower()
        return [p for p in self.products if search_term in p['name']]

    def edit_product(self, name=None, new_price=None, new_stock=None):
        """Edit an existing product's price and stock."""
        if None in (name, new_price, new_stock):  # Interactive mode
            name = input("Enter product name to edit: ").strip().lower()
            new_price = input(f"Enter new price for {name}: ")
            new_stock = input(f"Enter new stock for {name}: ")
        
        for product in self.products:
            if product['name'] == name.strip().lower():
                try:
                    new_price = float(new_price)
                    new_stock = int(new_stock)
                    if new_price < 0 or new_stock < 0:
                        return "Price and stock must be non-negative."
                        
                    product['price'] = new_price
                    product['stock'] = new_stock
                    self.write_file()
                    return f"Product '{name}' updated successfully."
                except ValueError:
                    return "Invalid input. Please enter valid numbers."
        return f"Product '{name}' not found."

    def remove_product(self, name=None):
        """Remove a product from the database."""
        if name is None:  # Interactive mode
            name = input("Enter the product name to remove: ").strip().lower()
        else:
            name = name.strip().lower()

        matching_products = [p for p in self.products if p['name'] == name]

        if not matching_products:
            return f"Product '{name}' not found."

        # Filter out the product to remove
        self.products = [p for p in self.products if p['name'] != name]
        self.write_file()
        return f"Product '{name}' removed successfully."
    
    def sort_products(self):
        """Sort products by specified field and order."""
        option = input("Sort by (name/price/stock): ").strip().lower()
        order = input("Sort order (asc/desc): ").strip().lower()
        reverse_order = (order == "desc")  # Determine sort direction

        if option in ["name", "price", "stock"]:
            try:
                # Sort with appropriate key function
                self.products.sort(
                    key=lambda x: (float(x[option]) if option in ["price", "stock"] else x[option]),
                    reverse=reverse_order
                )
                self.view_products()  # Display sorted results
            except Exception as e:
                print(f"Error sorting products: {e}")
        else:
            print("Invalid sorting option.")


    def filter_products(self, category):
        """Filter products by specified category."""
        category = category.strip().lower()
        filtered_products = [p for p in self.products if p['category'] == category]

        if not filtered_products:
            print(f"No products found in the '{category}' category.")
            return

        # Display filtered results
        print(f"\nProducts in the '{category}' category:")
        name_width = max(len(p["name"]) for p in filtered_products) + 2
        price_width = 10
        stock_width = 10

        print(f"{'Name'.ljust(name_width)} {'Price ($)'.ljust(price_width)} {'Stock'.ljust(stock_width)}")
        print("=" * (name_width + price_width + stock_width))

        for product in filtered_products:
            name = product['name'].title()
            price = f"${product['price']:.2f}"
            stock = str(product['stock'])
            print(f"{name.ljust(name_width)} {price.ljust(price_width)} {stock.ljust(stock_width)}")
        print(f"\nTotal Products in '{category}': {len(filtered_products)}")

    def export_inventory(self):
        """Export current inventory to a new CSV file."""
        export_filename = "exported_inventory.csv"
        try:
            with open(export_filename, mode='w', newline='') as file:
                fieldnames = ["name", "price", "stock", "category"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.products)
            print(f"Inventory exported successfully to {export_filename}.")
        except Exception as e:
            print(f"Error exporting inventory: {e}")

    @staticmethod
    def login():
        """Authenticate user and return their role (admin/user)."""
        print("\nLogin")
        username = input("Enter your ID (or press Enter to continue as a normal user): ").strip()

        if username == "":
            print("Logged in as a normal user.")
            return "user"

        try:
            with open("data.csv", mode='r', newline='') as file:
                reader = csv.DictReader(file)
                # Create dictionary of user data
                users = {
                    row['ID'].strip(): {
                        "name": row['Name'].strip(),
                        "age": row['Age'].strip(),
                        "gender": row['Gender'].strip(),
                        "program": row['Program'].strip()
                    } for row in reader
                }

                if username in users:
                    print(f"Login successful! Welcome, {users[username]['name']}.")
                    return "admin"
                else:
                    print("Invalid ID. Logged in as a normal user.")
                    return "user"
        except FileNotFoundError:
            print("User database not found. Logged in as a normal user.")
            return "user"
        except Exception as e:
            print(f"Error during login: {e}")
            return "user"


    def main_menu():
        """Main menu loop for the inventory management system."""
        db = ProductDatabase()  # Initialize database
        role = None  # Current user role

        while True:
            # Prompt for login if not already logged in
            if not role:
                role = ProductDatabase.login()

            # Display menu options based on user role
            print("\nInventory Management System")
            print("1. View Products")
            print("2. Search Product")
            print("3. Filter Products by Category")
            print("4. Sort Products")  # Available to all users
            if role == "admin":
                print("5. Add Product")
                print("6. Edit Product")
                print("7. Remove Product")
                print("8. Export Inventory")
            print("9. Logout")
            print("10. Exit")
            
            choice = input("Enter your choice: ").strip()

            # Handle menu choices
            if choice == "1":
                db.view_products()
            elif choice == "2":
                db.search_products()
            elif choice == "3":
                category = input("Enter category to filter by: ")
                db.filter_products(category)
            elif choice == "4":
                db.sort_products()
            elif role == "admin" and choice == "5":
                db.add_product()
            elif role == "admin" and choice == "6":
                db.edit_product()
            elif role == "admin" and choice == "7":
                db.remove_product()
            elif role == "admin" and choice == "8":
                db.export_inventory()
            elif choice == "9":
                print("Logging out...")
                role = None  # Reset role to force re-login
            elif choice == "10":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")


    if __name__ == "__main__":
        main_menu()  # Start the application