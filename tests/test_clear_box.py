import pytest
import os
import csv
from Stock import ProductDatabase
from UI2 import InventoryGUI
import tkinter as tk

@pytest.fixture
def setup_empty_file():
    """Fixture to create an empty Estock.csv file."""
    with open("Estock.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "stock", "category"])
        writer.writeheader()
    yield
    os.remove("Estock.csv")

def test_read_file_with_empty_file(setup_empty_file, capsys):
    """Test read_file() with an empty Estock.csv."""
    print("\n=== Testing read_file() with empty file ===")
    db = ProductDatabase()
    captured = capsys.readouterr()
    assert "File not found. Creating a new one." in captured.out
    assert db.products == []
    print("✓ Verified empty file handling works correctly")

def test_add_product_valid_input(capsys):
    """Test add_product() with valid input."""
    print("\n=== Testing add_product() with valid input ===")
    db = ProductDatabase()
    db.products = []
    result = db.add_product("test_product", "10.99", "5", "test")
    assert "added successfully" in result
    print("✓ Verified valid product addition")
    
    with open("Estock.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    assert len(rows) == 1
    assert rows[0]["name"] == "test_product"
    print("✓ Verified product appears in CSV file")

def test_add_product_duplicate(capsys):
    """Test add_product() with duplicate product."""
    print("\n=== Testing add_product() with duplicate ===")
    db = ProductDatabase()
    db.products = [{"name": "test", "price": 10.99, "stock": 5, "category": "test"}]
    result = db.add_product("test", "15.99", "10", "test")
    assert "already exists" in result
    print("✓ Verified duplicate product detection")

def test_edit_product_negative_values(capsys):
    """Test edit_product() with negative values."""
    print("\n=== Testing edit_product() with negative values ===")
    db = ProductDatabase()
    db.products = [{"name": "test", "price": 10.99, "stock": 5, "category": "test"}]
    result = db.edit_product("test", "-10", "5")
    assert "must be non-negative" in result
    print("✓ Verified negative value validation")

def test_gui_theme_toggle():
    """Test GUI theme toggle functionality."""
    print("\n=== Testing GUI theme toggle ===")
    root = tk.Tk()
    root.withdraw()  # Hide the window during tests
    gui = InventoryGUI(root)
    
    initial_theme = gui.current_theme
    gui.toggle_dark_mode()
    assert gui.current_theme != initial_theme
    print("✓ Verified theme toggle changes current theme")
    
    gui.toggle_dark_mode()
    assert gui.current_theme == initial_theme
    print("✓ Verified theme toggle cycles correctly")
    root.destroy()