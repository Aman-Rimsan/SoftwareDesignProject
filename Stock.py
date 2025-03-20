import csv

class ProductDatabase:
    def __init__(self, filename="Estock.csv"):
        self.filename = filename
        self.products = []
        self.read_file()

    def read_file(self):
            try:
                with open(self.filename, mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    self.products = [{"name": row["name"].strip().lower(),
                                    "price": float(row["price"]),
                                    "stock": int(row["stock"]),
                                    "category": row["category"].strip().lower()} for row in reader]
            except FileNotFoundError:
                print("File not found. Creating a new one.")
                self.write_file()
            except Exception as e:
             print(f"Error reading file: {e}")

    def write_file(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                fieldnames = ["name", "price", "stock", "category"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.products)
        except Exception as e:
            print(f"Error writing to file: {e}")

    def view_products(self):
            if not self.products:
                print("\nNo products available.")
                return

            # Calculate column widths dynamically
            name_width = max(len(p["name"]) for p in self.products) + 2
            price_width = 10
            stock_width = 10
            category_width = max(len(p["category"]) for p in self.products) + 2

            # Print header
            print("\nInventory:")
            print(f"{'Name'.ljust(name_width)} {'Price ($)'.ljust(price_width)} {'Stock'.ljust(stock_width)} {'Category'.ljust(category_width)}")
            print("=" * (name_width + price_width + stock_width + category_width))

            # Print product details
            for product in self.products:
                name = product['name'].title()  # Capitalize properly
                price = f"${product['price']:.2f}"
                stock = str(product['stock'])
                category = product['category'].title()  # Capitalize category
                print(f"{name.ljust(name_width)} {price.ljust(price_width)} {stock.ljust(stock_width)} {category.ljust(category_width)}")

            print(f"\nTotal Products: {len(self.products)}")

    def add_product(self):
        category = input("Enter product category (e.g., GPU, CPU, RAM, etc.): ").strip().lower()
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
        self.products.append({"name": name, "price": price, "stock": stock, "category": category})
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

    def remove_product(self):
            name = input("Enter the product name to remove: ").strip().lower()
            matching_products = [p for p in self.products if p['name'] == name]

            if not matching_products:
                print(f"Product '{name}' not found.")
                return

            self.products = [p for p in self.products if p['name'] != name]
            self.write_file()
            print(f"Product '{name}' removed successfully.")

    def sort_products(self):
        option = input("Sort by (name/price/stock): ").strip().lower()
        order = input("Sort order (asc/desc): ").strip().lower()
        reverse_order = True if order == "desc" else False

        if option in ["name", "price", "stock"]:
            try:
                self.products.sort(key=lambda x: (float(x[option]) if option in ["price", "stock"] else x[option]), reverse=reverse_order)
                self.view_products()
            except Exception as e:
                print(f"Error sorting products: {e}")
        else:
            print("Invalid sorting option.")

    def search_products(self):
        search_term = input("Enter product name to search: ").strip().lower()
        results = [p for p in self.products if search_term in p['name']]

        if not results:
            print("No matching products found.")
            return

        print("\nSearch Results:")
        print(f"{'Name'.ljust(20)} {'Price ($)'.ljust(10)} {'Stock'.ljust(10)}")
        print("=" * 40)

        for product in results:
            name = product['name'].title()
            price = f"${product['price']:.2f}"
            stock = str(product['stock'])
            print(f"{name.ljust(20)} {price.ljust(10)} {stock.ljust(10)}")
        print(f"\nTotal Matches: {len(results)}")
    
    def filter_products(self, category):
        category = category.strip().lower()
        filtered_products = [p for p in self.products if p['category'] == category]

        if not filtered_products:
            print(f"No products found in the '{category}' category.")
            return

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


def main_menu():
    db = ProductDatabase()
    while True:
        print("\nInventory Management System")
        print("1. View Products")
        print("2. Add Product")
        print("3. Edit Product")
        print("4. Remove Product")
        print("5. Sort Products")
        print("6. Search Product")
        print("7. Filter Products by Category")  # New option
        print("8. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            db.view_products()
        elif choice == "2":
            db.add_product()
        elif choice == "3":
            db.edit_product()
        elif choice == "4":
            db.remove_product()
        elif choice == "5":
            db.sort_products()
        elif choice == "6":
            db.search_products()
        elif choice == "7":
            category = input("Enter category to filter by: ")
            db.filter_products(category)
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()