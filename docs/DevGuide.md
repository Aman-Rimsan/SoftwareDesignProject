## Program Description
The program involves developing an inventory tracking system tailored for a tech company. It will include login/logout functionality, enabling users to view stored raw or sorted data and interact with the inventory by editing, deleting, adding, and viewing products. The system will not involve purchasing but will provide essential features for employees and administrators.

## Functionalities
* Reading & writing to a CSV file (Estock.csv) to persist product data (name, price, stock, category)

* Viewing: puts the inventory in a formatted table

* Adding: adds new products with input validation and duplicate checking

* Editing: edits existing products (price and stock)

* Removing: removes products by name

* Sorting: by name, price, or stock in ascending or descending order

* Searching: Search by name

* Filtering: Filter by category

* User interaction: Displays all the stock and has buttons for each functionality, also has a dark mode.

## Diagrams
![image](https://github.com/user-attachments/assets/793eb187-e0ff-4967-932e-bba2a9272a19)
![image](https://github.com/user-attachments/assets/9b2c41d0-d176-418d-b79c-676a48bf5ba2)


## Build
The E-Stock Inventory Management System can be built and run using several methods:

### Prerequisites
- Python 3.x
- Tkinter (included with most Python installations)

### Build Methods

#### 1. Using the Interactive Launcher (Recommended for Windows Users)
The system includes a user-friendly launcher that requires no command-line knowledge:
- Navigate to the project root directory
- Double-click `Run_Application.bat`
- Select the desired option from the menu:
  - Option 1: Run GUI Version
  - Option 2: Run Console Version
  - Option 3: Clean up files

#### 2. Using PowerShell (Windows)
For PowerShell users:
```powershell
.\run.ps1 gui      # Run GUI version
.\run.ps1 console  # Run console version
.\run.ps1 clean    # Clean up generated files
```

#### 3. Manual Python Execution
Run directly with Python:
```
python UI2.py      # Run GUI version
python Stock.py    # Run console version
```

### Building for Distribution
The system is designed to be run from source code, but can be packaged using PyInstaller if needed:
```
pip install pyinstaller
pyinstaller --onefile --windowed UI2.py
```

## Tests
The E-Stock Inventory Management System uses pytest for testing. The testing strategy follows a comprehensive approach with different types of tests:

### Test Types
1. **Clear Box Tests**: Tests that examine the internal workings of components
2. **Opaque Box Tests**: Tests that verify functionality without knowledge of implementation
3. **Translucent Box Tests**: Hybrid tests that combine aspects of both approaches

### Running Tests
To run all tests:
```
pytest tests/
```

To run specific test categories:
```
pytest tests/test_clear_box.py
pytest tests/test_opaque_box.py
pytest tests/test_translucent_box.py
```

### Test Coverage
Tests cover critical functionality including:
- Database operations (reading/writing to CSV)
- Product management (adding, editing, removing)
- User interface functionality
- Error handling and data validation
- Role-based access control

### Test-Driven Development
The project follows TDD principles where appropriate:
1. Write a failing test
2. Implement the feature to make the test pass
3. Refactor the code while maintaining passing tests

### Continuous Testing
For development, it's recommended to run tests after any significant changes to ensure system integrity and prevent regressions.

