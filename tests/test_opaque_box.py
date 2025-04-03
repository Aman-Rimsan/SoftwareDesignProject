import pytest
try:
    import tkinter as tk
    from UI2 import InventoryGUI
    tk_available = True
except ImportError:
    tk_available = False

from Stock import ProductDatabase
from UI2 import InventoryGUI
import tkinter as tk
from tkinter import messagebox
import csv
import os


def test_admin_vs_user_permissions(monkeypatch, capsys):
    """Test admin vs user role permissions."""
    print("\n=== Testing role-based permissions ===")
    
    # Mock the data.csv file
    with open("data.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Age", "Gender", "Program"])
        writer.writeheader()
        writer.writerow({"ID": "100920512", "Name": "Admin User", "Age": "30", "Gender": "M", "Program": "Admin"})
    
    # Test admin login
    print("Testing admin login...")
    monkeypatch.setattr("builtins.input", lambda _: "100920512")
    role = ProductDatabase.login()
    captured = capsys.readouterr()
    assert role == "admin"
    assert "Login successful" in captured.out
    print("✓ Verified admin login")
    
    # Test user login
    print("Testing user login...")
    monkeypatch.setattr("builtins.input", lambda _: "")
    role = ProductDatabase.login()
    captured = capsys.readouterr()
    assert role == "user"
    assert "normal user" in captured.out
    print("✓ Verified user login")
    
    os.remove("data.csv")

def test_search_functionality(capsys):
    """Test search functionality with partial matches."""
    print("\n=== Testing search functionality ===")
    db = ProductDatabase()
    db.products = [
        {"name": "processor", "price": 100.0, "stock": 10, "category": "cpu"},
        {"name": "gpu pro", "price": 200.0, "stock": 5, "category": "gpu"},
    ]
    
    print("Testing partial match search...")
    results = db.search_products("pro")
    assert len(results) == 2
    print("✓ Verified partial matching")
    
    print("Testing case insensitivity...")
    results = db.search_products("PRO")
    assert len(results) == 2
    print("✓ Verified case insensitivity")

@pytest.mark.skipif(not tk_available, reason="Tkinter not available")
def test_gui_admin_features(monkeypatch):
    """Test GUI admin-specific features."""
    print("\n=== Testing GUI admin features ===")
    root = tk.Tk()
    root.withdraw()
    
    # Mock admin login
    gui = InventoryGUI(root)
    
    # Simulate admin login by bypassing the login screen
    gui.role = "admin"
    gui.login_frame.destroy()  # Remove login frame
    gui.create_main_interface()  # Create main interface
    
    # Find the button frame
    button_texts = []
    for widget in gui.master.winfo_children():
        if isinstance(widget, tk.Frame):
            buttons = [w for w in widget.winfo_children() if isinstance(w, tk.Button)]
            button_texts = [b.cget("text") for b in buttons]
            break
    
    # Verify admin buttons are present
    admin_buttons = ["Add Product", "Edit Product", "Remove Product"]
    for button in admin_buttons:
        assert button in button_texts, f"Admin button '{button}' not found"
    
    print("✓ Verified all admin buttons appear")
    root.destroy()