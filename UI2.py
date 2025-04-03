import csv
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class ProductDatabase:
    def __init__(self, filename="Estock.csv"):
        self.filename = filename
        self.products = []
        self.read_file()

    def read_file(self):
        """Read products from the CSV file."""
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.products = [dict(row) for row in reader]
                for product in self.products:
                    product["price"] = float(product["price"])
                    product["stock"] = int(product["stock"])
        except FileNotFoundError:
            self.write_file()
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {e}")

    def write_file(self):
        """Write products to the CSV file."""
        try:
            with open(self.filename, mode='w', newline='') as file:
                fieldnames = ["name", "price", "stock", "category"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.products)
        except Exception as e:
            messagebox.showerror("Error", f"Error writing to file: {e}")

    def add_product(self, name, price, stock, category):
        """Add a new product to the database."""
        name = name.strip().lower()
        category = category.strip().lower()
        if any(p['name'] == name and p['category'] == category for p in self.products):
            return "Product already exists in this category."
        try:
            price = float(price)
            stock = int(stock)
            if price < 0 or stock < 0:
                return "Price and stock must be non-negative."
        except ValueError:
            return "Invalid input. Price must be a number, stock must be an integer."
        
        self.products.append({"name": name, "price": price, "stock": stock, "category": category})
        self.write_file()
        return f"Product '{name}' added successfully."

    def edit_product(self, name, new_price, new_stock):
        """Edit an existing product."""
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

    def search_products(self, search_term):
        """Search for products by name."""
        search_term = search_term.strip().lower()
        return [p for p in self.products if search_term in p['name']]

    def filter_products(self, category):
        """Filter products by category."""
        category = category.strip().lower()
        return [p for p in self.products if p['category'] == category]

    def sort_products(self, sort_by, order):
        """Sort products by a given field and order."""
        reverse_order = (order == "desc")
        try:
            self.products.sort(
                key=lambda x: x[sort_by] if sort_by in ["name", "category"] else float(x[sort_by]),
                reverse=reverse_order
            )
            return "Products sorted successfully."
        except Exception as e:
            return f"Error sorting products: {e}"

    def get_all_products(self):
        """Get all products."""
        return self.products.copy()

    def export_inventory(self):
        """Export inventory to a CSV file."""
        export_filename = "exported_inventory.csv"
        try:
            with open(export_filename, mode='w', newline='') as file:
                fieldnames = ["name", "price", "stock", "category"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.products)
            return f"Inventory exported successfully to {export_filename}."
        except Exception as e:
            return f"Error exporting inventory: {e}"


class InventoryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")
        self.db = ProductDatabase()
        self.role = "customer"  # Default role is customer
        self.admin_data = self.load_admin_data()
        
        # Define color schemes
        self.light_mode = {
            'bg': 'white',
            'fg': 'black',
            'button_bg': 'lightgray',
            'button_fg': 'black',
            'tree_bg': 'white',
            'tree_fg': 'black',
            'tree_heading_bg': 'lightgray',
            'tree_heading_fg': 'black'
        }
        self.dark_mode = {
            'bg': 'gray10',
            'fg': 'white',
            'button_bg': 'gray20',
            'button_fg': 'white',
            'tree_bg': 'gray20',
            'tree_fg': 'white',
            'tree_heading_bg': 'gray30',
            'tree_heading_fg': 'white'
        }
        self.current_theme = self.light_mode

        # Create login frame first
        self.create_login_frame()
        
    def load_admin_data(self):
        """Load admin data from data.csv file."""
        try:
            with open('data.csv', mode='r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            messagebox.showerror("Error", "Admin data file not found.")
            return []
        except Exception as e:
            messagebox.showerror("Error", f"Error reading admin data: {e}")
            return []

    def create_login_frame(self):
        """Create the login frame."""
        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack(pady=50)
        
        tk.Label(self.login_frame, text="Inventory Management System", font=('Arial', 16)).grid(row=0, columnspan=2, pady=10)
        
        tk.Label(self.login_frame, text="Admin ID:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.id_entry = tk.Entry(self.login_frame)
        self.id_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(self.login_frame, text="Login as Admin", command=self.authenticate).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.login_frame, text="Continue as Customer", command=self.set_customer_role).grid(row=3, columnspan=2, pady=5)

    def authenticate(self):
        """Authenticate the user using only ID."""
        user_id = self.id_entry.get().strip()
        
        if not user_id:
            messagebox.showwarning("Warning", "Please enter an ID")
            return
            
        for admin in self.admin_data:
            if str(admin['ID']).strip() == user_id:
                self.role = "admin"
                self.login_frame.destroy()
                self.create_main_interface()
                messagebox.showinfo("Success", "Logged in as Admin")
                return
                
        messagebox.showerror("Error", "Invalid ID. Continuing as Customer.")
        self.set_customer_role()

    def set_customer_role(self):
        """Set the user role to customer and proceed."""
        self.role = "customer"
        self.login_frame.destroy()
        self.create_main_interface()
        messagebox.showinfo("Info", "Logged in as Customer")

    def create_main_interface(self):
        """Create the main UI widgets."""
        # Menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)
        
        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Logout", command=self.logout)
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Treeview to display products
        self.tree = ttk.Treeview(self.master, columns=('Name', 'Price', 'Stock', 'Category'), show='headings')
        self.tree.heading('Name', text='Product Name')
        self.tree.heading('Price', text='Price ($)')
        self.tree.heading('Stock', text='Stock')
        self.tree.heading('Category', text='Category')
        self.tree.column('Name', width=200)
        self.tree.column('Price', width=100)
        self.tree.column('Stock', width=100)
        self.tree.column('Category', width=150)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

        # Button frame
        button_frame = tk.Frame(self.master)
        button_frame.pack(fill='x', padx=10, pady=10)

        buttons = [
            ('Add Product', self.open_add_window if self.role == "admin" else None),
            ('Edit Product', self.open_edit_window if self.role == "admin" else None),
            ('Remove Product', self.open_remove_window if self.role == "admin" else None),
            ('Sort Products', self.open_sort_window),
            ('Search Products', self.open_search_window),
            ('Filter Products', self.open_filter_window),
            ('Export Inventory', self.export_inventory if self.role == "admin" else None),
            ('Refresh', self.update_display),
            ('Toggle Dark Mode', self.toggle_dark_mode),
            ('Exit', self.master.quit)
        ]

        for text, command in buttons:
            if command:  # Only add buttons with valid commands
                tk.Button(button_frame, text=text, command=command).pack(side='left', padx=5)

        self.apply_theme()
        self.update_display()

    def logout(self):
        """Log out and return to login screen."""
        # Clear all widgets
        for widget in self.master.winfo_children():
            widget.destroy()
        
        # Reset to default theme
        self.current_theme = self.light_mode
        
        # Recreate login interface
        self.role = "customer"
        self.create_login_frame()

    def apply_theme(self):
        """Apply the selected theme to the UI."""
        self.master.config(bg=self.current_theme['bg'])

        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.config(bg=self.current_theme['bg'])
                for child in widget.winfo_children():
                    if isinstance(child, tk.Button):
                        child.config(bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'])
            elif isinstance(widget, ttk.Treeview):
                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                              background=self.current_theme['tree_bg'],
                              foreground=self.current_theme['tree_fg'],
                              fieldbackground=self.current_theme['tree_bg'])
                style.configure("Treeview.Heading",
                              background=self.current_theme['tree_heading_bg'],
                              foreground=self.current_theme['tree_heading_fg'],
                              font=('Arial', 10, 'bold'))
                widget.config(style="Treeview")

    def toggle_dark_mode(self):
        """Toggle between light and dark mode."""
        self.current_theme = self.dark_mode if self.current_theme == self.light_mode else self.light_mode
        self.apply_theme()

    def update_display(self, products=None):
        """Update the Treeview with the latest product data."""
        if products is None:
            products = self.db.get_all_products()
            
        for item in self.tree.get_children():
            self.tree.delete(item)
        for product in products:
            self.tree.insert('', 'end', values=(
                product['name'].title(),
                f"${product['price']:.2f}",
                product['stock'],
                product['category'].title()
            ))

    def open_add_window(self):
        """Open a window to add a new product."""
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Product")

        tk.Label(add_window, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Price:").grid(row=1, column=0, padx=5, pady=5)
        price_entry = tk.Entry(add_window)
        price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Stock:").grid(row=2, column=0, padx=5, pady=5)
        stock_entry = tk.Entry(add_window)
        stock_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Category:").grid(row=3, column=0, padx=5, pady=5)
        category_entry = tk.Entry(add_window)
        category_entry.grid(row=3, column=1, padx=5, pady=5)

        def submit():
            result = self.db.add_product(
                name_entry.get(),
                price_entry.get(),
                stock_entry.get(),
                category_entry.get()
            )
            messagebox.showinfo("Result", result)
            add_window.destroy()
            self.update_display()

        tk.Button(add_window, text="Submit", command=submit).grid(row=4, columnspan=2, pady=10)

    def open_edit_window(self):
        """Open a window to edit an existing product."""
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

    def open_remove_window(self):
        """Open a window to remove a product."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a product to remove.")
            return

        product_name = self.tree.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to remove {product_name}?")
        if confirm:
            # Find and remove the product from the database
            for i, product in enumerate(self.db.products):
                if product['name'].title() == product_name:
                    del self.db.products[i]
                    self.db.write_file()
                    messagebox.showinfo("Success", f"Product '{product_name}' removed successfully.")
                    self.update_display()
                    return
            messagebox.showerror("Error", f"Product '{product_name}' not found in database.")

    def open_sort_window(self):
        """Open a window to select sorting options."""
        sort_window = tk.Toplevel(self.master)
        sort_window.title("Sort Products")

        tk.Label(sort_window, text="Sort by:").grid(row=0, column=0, padx=5, pady=5)
        sort_by_var = tk.StringVar(value="name")
        tk.OptionMenu(sort_window, sort_by_var, "name", "price", "stock", "category").grid(row=0, column=1, padx=5, pady=5)

        tk.Label(sort_window, text="Order:").grid(row=1, column=0, padx=5, pady=5)
        order_var = tk.StringVar(value="asc")
        tk.OptionMenu(sort_window, order_var, "asc", "desc").grid(row=1, column=1, padx=5, pady=5)

        def submit():
            result = self.db.sort_products(sort_by_var.get(), order_var.get())
            messagebox.showinfo("Result", result)
            sort_window.destroy()
            self.update_display()

        tk.Button(sort_window, text="Sort", command=submit).grid(row=2, columnspan=2, pady=10)

    def open_search_window(self):
        """Open a window to search for products."""
        search_term = simpledialog.askstring("Search Products", "Enter product name to search:")
        if search_term:
            results = self.db.search_products(search_term)
            if results:
                self.update_display(results)
            else:
                messagebox.showinfo("Search Results", "No products found matching your search.")

    def open_filter_window(self):
        """Open a window to filter products by category."""
        categories = list(set(product['category'] for product in self.db.products))
        if not categories:
            messagebox.showinfo("Info", "No categories available.")
            return

        filter_window = tk.Toplevel(self.master)
        filter_window.title("Filter Products")

        tk.Label(filter_window, text="Select Category:").pack(padx=5, pady=5)
        category_var = tk.StringVar(value=categories[0])
        tk.OptionMenu(filter_window, category_var, *categories).pack(padx=5, pady=5)

        def submit():
            results = self.db.filter_products(category_var.get())
            filter_window.destroy()
            self.update_display(results)

        tk.Button(filter_window, text="Filter", command=submit).pack(pady=10)

    def export_inventory(self):
        """Export the inventory to a CSV file."""
        result = self.db.export_inventory()
        messagebox.showinfo("Export Result", result)


if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()