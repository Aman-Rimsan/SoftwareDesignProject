import csv 

# Open and read the CSV file
with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)  # Read file as a dictionary
    data = [row for row in csv_reader]  # Store CSV content in a list of dictionaries

# Display menu options
print("1. Display items")
print("2. Edit existing item")
print("3. Add new item")
print("4. Exit program")
user_input = int(input("Enter: "))  # Get user choice

# Loop until user chooses to exit
while user_input != 4:
    if user_input == 1:
        # Display all items in the CSV file
        for row in data:
            for key, value in row.items():
                print(f"{key}: {value}", end=" ")  # Print key-value pairs
            print()  # New line after each row
    elif user_input == 2:
        # Edit an existing item
        print("Which person you like to edit? (Type the name): ")
        name = input("Enter: ").strip()
        print("What would you like to edit? [Name, Age, ID, Gender, Program]")
        change = input("Enter: ").strip()
        print("What should it be? ")
        changed_item = input("Enter: ").strip()
        
        # Search for the person by name and update the specified field
        for row in data:
            if row["Name"].lower() == name.lower():
                row[change] = changed_item
    elif user_input == 3:
        # Add a new item to the data list
        name = input("Enter name: ").strip()
        age = input("Enter age: ").strip()
        identity = input("Enter id: ").strip()
        gender = input("Enter gender: ").strip()
        program = input("Enter program: ").strip()

        new_item = {
            "Name": name,
            "Age": age,
            "ID": identity,
            "Gender": gender,
            "Program": program
        }
        data.append(new_item)  # Append new data entry
        print("New item added successfully.")

    # Reprint menu after an operation
    print("\n1. Display items")
    print("2. Edit existing item")
    print("3. Add new item")
    print("4. Exit program")
    user_input = int(input("Enter: "))

# Save modified data back to the CSV file
with open('data.csv', 'w', newline='') as file:
    fieldnames = data[0].keys()  # Get field names from the first dictionary entry
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()  # Write the header row
    csv_writer.writerows(data)  # Write all rows back to the CSV file

print("Program exited.")