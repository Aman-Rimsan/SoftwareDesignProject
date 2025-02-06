import csv

with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

print("1. Display items")
print("2. Edit existing item")
print("3. Add new item")
print("4. Exit program")
user_input = int(input("Enter: "))

while user_input != 4:
    if user_input == 1:
        for row in data:
            for key, value in row.items():
                print(f"{key}: {value}", end=" ")
            print()
    elif user_input == 2:
        print("Which person you like to edit? (Type the name): ")
        name = input("Enter: ").strip()
        print("What would you like to edit? [Name, Age, ID, Gender, Program]")
        change = input("Enter: ").strip()
        print("What should it be? ")
        changed_item = input("Enter: ").strip()
        for row in data:
            if row["Name"].lower() == name.lower():
                row[change] = changed_item
    elif user_input == 3:
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
        data.append(new_item)
        print("New item added successfully.")

    print("\n1. Display items")
    print("2. Edit existing item")
    print("3. Add new item")
    print("4. Exit program")
    user_input = int(input("Enter: "))

with open('data.csv', 'w', newline='') as file:
    fieldnames = data[0].keys()
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print("Program exited.")
