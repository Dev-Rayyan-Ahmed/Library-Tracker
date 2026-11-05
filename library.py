# library.py
# A simple command-line library tracker.
books = {}  # title -> {"author": str, "available": bool}
def show_menu():
    print("\n=== Library Tracker ===")
    print("0. Exit")
    print("1. Add a Book")
    print("2. List all Book")
    print("3. Borrow Book")
    print("4. return a book")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            lower_title = title.lower()
            
            if any(k.lower() == lower_title for k in books.keys()):
                print(f'"{title}" is already in the library.')
            else:
                books[title] = {"author": author, "available": True}
                print(f'Added "{title}".')
                
        elif choice == "2":
            if not books:
                print("There are no books.")
            else:
                for t, info in books.items():
                    status = "Available" if info["available"] else "Borrowed"
                    print(f'{t} by {info["author"]}\n{status}')
        elif choice == "4":
            title = input("Title: ")
            if title not in books:
                print(f'No book titled "{title}".')
            elif books[title]["available"]:
                print(f'"{title}" is not borrowed.')
            else:
                books[title]["available"] = True
                print(f'You returned "{title}".')    
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
