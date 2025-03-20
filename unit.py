import unittest
from unittest.mock import MagicMock
from Stock import ProductDatabase  # Assuming this is your class

class TestProductDatabase(unittest.TestCase):
    def setUp(self):
        self.db = ProductDatabase("test.csv")
        self.db.read_file = MagicMock(return_value=None)

    def test_add_product(self):
        self.db.add_product = MagicMock()
        self.db.add_product("Laptop", 999.99, 10)
        self.db.add_product.assert_called_with("Laptop", 999.99, 10)

    def test_view_products(self):
        self.db.view_products = MagicMock()
        self.db.view_products()
        self.db.view_products.assert_called()

    def test_write_file(self):
        self.db.write_file = MagicMock()
        self.db.write_file()
        self.db.write_file.assert_called()
    
    def test_read_file(self):
        self.db.read_file = MagicMock()
        self.db.read_file()
        self.db.read_file.assert_called()


if __name__ == "__main__":
    unittest.main()
