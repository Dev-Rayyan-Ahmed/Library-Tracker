# library.py
# A simple command-line library tracker.
books = {}  # title -> {"author": str, "available": bool}
def show_menu():
    print("\n=== Library Tracker ===")
    print("0. Exit")
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "3":
            title = input("Title: ")
            lower_title = title.lower()
            found_key = next((k for k in books.keys() if k.lower() == lower_title), None)
            
            if not found_key:
                print(f'No book titled "{title}".')
            elif not books[found_key]["available"]:
                print(f'"{title}" is already borrowed.')
            else:
                books[found_key]["available"] = False
                print(f'You borrowed "{title}".')
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
