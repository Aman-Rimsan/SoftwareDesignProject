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
Python, Tkinter (for GUI)

## How To Run
- First go to your terminal and go to the desired file where you want to clone the repository
- Once you're in the desired file type the command **git clone** with the url **https://github.com/Aman-Rimsan/SoftwareDesignProject.git**
- Now that you've cloned the repository go into the github file and type **code .**, this will open all the files in the repo in your default IDE. We are using vscode as our IDE.
- Now that your IDE is up, you can either run the terminal version of the software in **Stock.py** or the GUI version in **UI2.py**
### IDE
- Simply run the python files the way your IDE would want to, for vscode there is a play button near the top right of your screen
### Packaged Executable
- To run the packaged executable simply type `Run_Application.bat` in the terminal
- Once ran the terminal will ask whether you want to run the terminal version or GUI version of the application

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

### Variables
| Variable       | Default Value | Description                          |
|----------------|---------------|--------------------------------------|
| `PYTHON`       | `python`      | Python interpreter to use            |
| `STOCK_SCRIPT` | `Stock.py`    | Console version script               |
| `UI_SCRIPT`    | `UI2.py`      | Graphical interface version script   |

## Available Commands

### `make console`
Runs the console version of the Inventory Management System (`Stock.py`).

**Example:**
```bash
make console
```

### `make gui`

Runs the graphical user interface version (UI2.py). This is the recommended version for most users.

Example:
```bash
make gui
```

### `make clean`

Cleans up generated files while preserving original data files.

Actions:

    Removes exported_inventory.csv if it exists

    Preserves original data files (Estock.csv, data.csv)

Example:
```bash
make clean
```

### `make help`

Displays help message with all available commands.

Example:
```bash
make help
```
