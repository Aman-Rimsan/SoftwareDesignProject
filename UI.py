import csv
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class ProductDatabase:
    def __init__(self, filename="Estock.csv"):
        self.filename = filename
        self.products = []
        self.read_file()

    def read_file(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.products = [{
                    "name": row["name"].strip().lower(),
                    "price": float(row["price"]),
                    "stock": int(row["stock"])
                } for row in reader]
        except FileNotFoundError:
            self.write_file()
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {e}")

    def write_file(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                fieldnames = ["name", "price", "stock"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.products)
        except Exception as e:
            messagebox.showerror("Error", f"Error writing to file: {e}")

    def add_product(self, name, price, stock):
        name = name.strip().lower()
        if any(p['name'] == name for p in self.products):
            return "Product already exists."
        try:
            price = float(price)
            stock = int(stock)
            if price < 0 or stock < 0:
                return "Price and stock must be non-negative."
        except ValueError:
            return "Invalid input. Price must be a number, stock must be an integer."
        
        self.products.append({"name": name, "price": price, "stock": stock})
        self.write_file()
        return f"Product '{name}' added successfully."

    def edit_product(self, name, new_price, new_stock):
        name = name.strip().lower()
        for product in self.products:
            if product['name'] == name:
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

    def remove_product(self, name):
        name = name.strip().lower()
        initial_count = len(self.products)
        self.products = [p for p in self.products if p['name'] != name]
        if len(self.products) < initial_count:
            self.write_file()
            return f"Product '{name}' removed successfully."
        return f"Product '{name}' not found."

    def sort_products(self, option, order):
        reverse_order = (order == "desc")
        try:
            self.products.sort(
                key=lambda x: x[option] if option == "name" else float(x[option]),
                reverse=reverse_order
            )
            return "Products sorted successfully."
        except Exception as e:
            return f"Error sorting products: {e}"

    def search_products(self, search_term):
        search_term = search_term.strip().lower()
        return [p for p in self.products if search_term in p['name']]

    def get_all_products(self):
        return self.products.copy()

class InventoryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")
        self.db = ProductDatabase()

        # Configure main window layout
        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        # Treeview to display products
        self.tree = ttk.Treeview(self.master, columns=('Name', 'Price', 'Stock'), show='headings')
        self.tree.heading('Name', text='Product Name')
        self.tree.heading('Price', text='Price ($)')
        self.tree.heading('Stock', text='Stock')
        self.tree.column('Name', width=200)
        self.tree.column('Price', width=100)
        self.tree.column('Stock', width=100)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

        # Button frame
        button_frame = tk.Frame(self.master)
        button_frame.pack(fill='x', padx=10, pady=10)

        buttons = [
            ('Add Product', self.open_add_window),
            ('Edit Product', self.open_edit_window),
            ('Remove Product', self.remove_product),
            ('Sort Products', self.open_sort_window),
            ('Search Products', self.open_search_window),
            ('Refresh', self.update_display),
            ('Exit', self.master.quit)
        ]

        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command).pack(side='left', padx=5)

    def update_display(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for product in self.db.get_all_products():
            self.tree.insert('', 'end', values=(
                product['name'].title(),
                f"${product['price']:.2f}",
                product['stock']
            ))

    def open_add_window(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add New Product")

        tk.Label(add_window, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Price:").grid(row=1, column=0, padx=5, pady=5)
        price_entry = tk.Entry(add_window)
        price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Stock:").grid(row=2, column=0, padx=5, pady=5)
        stock_entry = tk.Entry(add_window)
        stock_entry.grid(row=2, column=1, padx=5, pady=5)

        def submit():
            result = self.db.add_product(
                name_entry.get(),
                price_entry.get(),
                stock_entry.get()
            )
            messagebox.showinfo("Result", result)
            add_window.destroy()
            self.update_display()

        tk.Button(add_window, text="Submit", command=submit).grid(row=3, columnspan=2, pady=10)

    def open_edit_window(self):
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Product")

        tk.Label(edit_window, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(edit_window, text="New Price:").grid(row=1, column=0, padx=5, pady=5)
        price_entry = tk.Entry(edit_window)
        price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(edit_window, text="New Stock:").grid(row=2, column=0, padx=5, pady=5)
        stock_entry = tk.Entry(edit_window)
        stock_entry.grid(row=2, column=1, padx=5, pady=5)

        def submit():
            result = self.db.edit_product(
                name_entry.get(),
                price_entry.get(),
                stock_entry.get()
            )
            messagebox.showinfo("Result", result)
            edit_window.destroy()
            self.update_display()

        tk.Button(edit_window, text="Submit", command=submit).grid(row=3, columnspan=2, pady=10)

    def remove_product(self):
        name = simpledialog.askstring("Remove Product", "Enter product name to remove:")
        if name:
            result = self.db.remove_product(name)
            messagebox.showinfo("Result", result)
            self.update_display()

    def open_sort_window(self):
        sort_window = tk.Toplevel(self.master)
        sort_window.title("Sort Products")

        tk.Label(sort_window, text="Sort by:").grid(row=0, column=0, padx=5, pady=5)
        sort_by = ttk.Combobox(sort_window, values=["name", "price", "stock"])
        sort_by.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(sort_window, text="Order:").grid(row=1, column=0, padx=5, pady=5)
        sort_order = ttk.Combobox(sort_window, values=["asc", "desc"])
        sort_order.grid(row=1, column=1, padx=5, pady=5)

        def submit():
            result = self.db.sort_products(sort_by.get(), sort_order.get())
            messagebox.showinfo("Result", result)
            sort_window.destroy()
            self.update_display()

        tk.Button(sort_window, text="Sort", command=submit).grid(row=2, columnspan=2, pady=10)

    def open_search_window(self):
        search_term = simpledialog.askstring("Search Products", "Enter product name:")
        if search_term:
            results = self.db.search_products(search_term)
            if not results:
                messagebox.showinfo("Search Results", "No products found!")
            else:
                # Create new window for search results
                result_window = tk.Toplevel(self.master)
                result_window.title("Search Results")
                
                tree = ttk.Treeview(result_window, columns=('Name', 'Price', 'Stock'), show='headings')
                tree.heading('Name', text='Product Name')
                tree.heading('Price', text='Price ($)')
                tree.heading('Stock', text='Stock')
                
                for product in results:
                    tree.insert('', 'end', values=(
                        product['name'].title(),
                        f"${product['price']:.2f}",
                        product['stock']
                    ))
                
                tree.pack(fill='both', expand=True, padx=10, pady=10)
                tk.Label(result_window, text=f"Found {len(results)} matching products").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()