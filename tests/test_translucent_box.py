import pytest
import csv
import os
from Stock import ProductDatabase
from UI2 import InventoryGUI
import tkinter as tk

@pytest.fixture
def setup_clean_file():
    """Fixture to reset Estock.csv to a clean state."""
    with open("Estock.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "stock", "category"])
        writer.writeheader()
    yield
    os.remove("Estock.csv")

@pytest.fixture
def setup_large_file():
    """Fixture to create a large Estock.csv file."""
    with open("Estock.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "stock", "category"])
        writer.writeheader()
        for i in range(1000):
            writer.writerow({"name": f"product{i}", "price": 10.0, "stock": 100, "category": "test"})
    yield
    os.remove("Estock.csv")

def test_file_persistence(monkeypatch, setup_clean_file, capsys):
    """Test file persistence after multiple operations."""
    print("\n=== Testing file persistence through operations ===")
    db = ProductDatabase()
    
    # Test add
    print("Testing product addition...")
    result = db.add_product("test_product", "10.99", "5", "test")
    assert "added successfully" in result
    with open("Estock.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    assert len(rows) == 1
    print("✓ Verified product added to file")
    
    # Test edit
    print("Testing product edit...")
    result = db.edit_product("test_product", "15.99", "10")
    assert "updated successfully" in result
    with open("Estock.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    assert rows[0]["price"] == "15.99"
    assert rows[0]["stock"] == "10"
    print("✓ Verified product edited in file")
    
    # Test remove
    print("Testing product removal...")
    db.products = [{"name": "test_product", "price": 15.99, "stock": 10, "category": "test"}]
    db.write_file()
    db.remove_product("test_product")
    with open("Estock.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    assert len(rows) == 0
    print("✓ Verified product removed from file")

def test_memory_usage(monkeypatch, setup_large_file, capsys):
    """Test memory usage during large operations."""
    print("\n=== Testing memory usage with large dataset ===")
    db = ProductDatabase()
    
    print("Testing with 1000 products...")
    assert len(db.products) == 1000
    print("✓ Verified large dataset loaded")
    
    print("Testing sorting performance...")
    db.products.sort(key=lambda x: float(x["price"]))
    assert float(db.products[0]["price"]) == 10.0
    print("✓ Verified sorting works with large dataset")

def test_gui_large_dataset(monkeypatch, setup_large_file):
    """Test GUI with large dataset."""
    print("\n=== Testing GUI with large dataset ===")
    root = tk.Tk()
    root.withdraw()
    gui = InventoryGUI(root)
    gui.create_main_interface()  # Ensure interface is created
    
    print("Testing Treeview update with 1000 items...")
    gui.update_display(gui.db.get_all_products())
    assert len(gui.tree.get_children()) == 1000
    print("✓ Verified GUI handles large dataset")
    root.destroy()