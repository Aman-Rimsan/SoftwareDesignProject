import os
import subprocess

def run_stock():
    subprocess.run(["python", "Stock.py"])

def run_ui():
    subprocess.run(["python", "UI2.py"])

def install_dependencies():
    if os.path.exists("requirements.txt"):
        subprocess.run(["python", "-m", "pip", "install", "-r", "requirements.txt"])
    else:
        print("No requirements.txt found. Skipping dependency installation.")

def clean():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith(".pyc"):
                os.remove(os.path.join(root, name))
        for name in dirs:
            if name == "__pycache__":
                os.rmdir(os.path.join(root, name))
    print("Cleanup complete.")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Run Stock.py")
        print("2. Run UI2.py")
        print("3. Install dependencies")
        print("4. Clean up temporary files")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            run_stock()
        elif choice == "2":
            run_ui()
        elif choice == "3":
            install_dependencies()
        elif choice == "4":
            clean()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()