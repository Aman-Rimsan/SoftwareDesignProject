# SoftwareDesignProject

## Project description
The project involves developing an inventory tracking system tailored for a tech company. It will include login/logout functionality, enabling users to view stored raw or sorted data and interact with the inventory by editing, deleting, adding, and viewing products. The system will not involve purchasing but will provide essential features for employees and administrators.

## Roles 
Project Manager: Abbas Akbar

Technical Manager: Amanulla Mohammed Rimsan

Front-End Lead: Lesley Ozurigbo

Back-End Lead: Abdul Ghafour Ahmed

Software Quality Lead: Ze Yu Shi

Developers: All

## Software Notes
The customer requires a software system designed for internal use by a tech company. The software will read a large file containing information about the inventory of the customer's computer stocks, price, name, etc. It will then count the number of each product in stock and sort it. The customer has decided to allow us to determine how to sort the products. The system will allow admins to search, add, edit, remove, and sort products. While employees can only view, sort, and search for products. This software will not be designed for use by customers, it is a company-only software used for inventory tracking. The UI of the software will be completely determined by the development team as the customer has no preferences

## Features
View Products: Displays all products with their name, price, and stock quantity.

Add Product: Allows users to add new products to the inventory.

Edit Product: Enables modifications to the price and stock of existing products.

Search Products: Allows users to find products by name or keyword.

Filter Products: Allow user to search the product by the range of minimum and maximum stock

Persistent Storage: Uses a CSV file (Estock.csv) to store product data.

## Installation
Python

## Setup
Clone the Repository: Download the project files from GitHub or another source.

Ensure Estock.csv Exists

Run the Script

## Usage
Inventory Management System
1. View Products
2. Add Product
3. Edit Product
4. Search Products
5. Filter Products
6. Exit

Option 1: Displays the inventory.

Option 2: Prompts for product details and adds them to the inventory.

Option 3: Allows editing of an existing product’s price or stock quantity.

Option 4: Searches for products based on user input.

Option 5: Using filter to allow user to find the stock by the range of it

Option 6: Exits the program.

## Makefile
This project includes a Makefile to simplify running scripts and managing the environment. Below is a breakdown of the available commands and what each one does:

Variables

1. PYTHON: Specifies the Python interpreter to use (default is python).
2. STOCK_SCRIPT: The Python script that runs stock-related logic (Stock.py).
3. UI_SCRIPT: The Python script for the user interface (UI2.py).
4. REQUIREMENTS: The dependencies file (requirements.txt).

Available Commands
1. make run_stock
- Runs the Stock.py script.

2. make run_ui
- Runs the UI2.py script. This is the default command when you run make without arguments.

3. make install
- Installs dependencies listed in requirements.txt. If the file is not found, it skips installation and shows a message.

4. make clean
- Removes temporary files like .pyc files and the __pycache__ directory to clean up the workspace.

5. make help
- Displays a list of available commands and their descriptions.

