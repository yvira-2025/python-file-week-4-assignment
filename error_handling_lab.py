# error_handling_lab.py

filename = input("📂 Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        print("\n📄 File contents:\n")
        print(file.read())

except FileNotFoundError:
    print(f"❌ File '{filename}' not found. Please check the name and try again.")
except PermissionError:
    print(f"🚫 You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
