from book import Book
from cart import ShoppingCart
from user import User


print("\nWelcome to your online book retailer!\n")
#stocking virtual shelf
Book.addBook("1984","George Orwell",15,"available")
Book.addBook("of mice and men","John Steinbeck",10,"unavailable")
Book.addBook("anna karenina","Leo Tolstoy",20,"available")

print("Current book stock:")
for book, details in Book.Books.items():  
    print(f"   {book} - by {details.author}, ${details.price}, {details.status}")

while True:
    action = input("\nWhat action would you like to take? sign in, register, del, list users, quit\n").strip()
    
    if action.lower() == "register":
        User.registerUser()
    
    elif action.lower() == "del":
        User.deleteUser()
    
    elif action.lower() == "sign in":
        pass
        user = User.signIn()
        if user:
            print("\nWelcome to your account!\n")
            while True:
                action = input("What action would you like to take with your cart? add, remove, list catalog, check cart, checkout, logout\n").strip().lower()
                
                if action.lower() == "add":
                    print("\nOk lets add a book to your cart...\n")
                    print("Current book stock:")
                    for book, details in Book.Books.items():  
                        print(f"   {book} - by {details.author}, ${details.price}, {details.status}")
                    
                    bookName = input("\nWhich book would you like to add?\n").strip()
                    if bookName.lower() in Book.Books:
                        if Book.Books[bookName].status == "available":
                            ShoppingCart.addBook(user, Book.Books[bookName])
                            Book.Books[bookName].status = "unavailable"
                            print(f"\n{bookName} succesfully added to your cart!\n")
                        else:
                            print("\nSorry that book isn't available\n")
                    else:
                        print("\nSorry, that book isn't in our catalog!\n")
                
                elif action.lower() == "remove":
                    print("\nOk lets remove a book to your cart...")
                    print("Here's what's in your cart...\n")
                    
                    if user.cart:
                        ShoppingCart.listContents(user.cart)
                        bookName = input("\nWhich book would you like to remove?\n").strip()
                        
                        if bookName in user.cart.contents:
                            ShoppingCart.removeBook(user, Book.Books[bookName])
                            Book.Books[bookName].status = "available"
                            print(f"\n{bookName} succesfully removed from your cart!\n")
                        else:
                            print("\nSorry that book isn't available\n")
                    else:
                        print("\nSorry, it doesn't look like you have any books in your cart!\n")
                
                elif action.lower() == "list catalog":
                    print("Current book stock:")
                    for book, details in Book.Books.items():  
                        print(f"   {book} - by {details.author}, ${details.price}, {details.status}")
                
                elif action.lower() == "checkout":
                    
                    print("\nOk lets go to the checkout...\n")
                    if user.cart:
                        ShoppingCart.checkout(user.cart)
                    else:
                        print("\nIt doesn't look like you've added anything to your cart yet...\n")
                
                elif action.lower() == "check cart":
                    
                    print("\nOk lets see what's in your cart...\n")
                    if user.cart:
                        ShoppingCart.listContents(user.cart)
                    else:
                        print("\nIt doesn't look like you've added anything to your cart yet...\n")
                    pass
                
                elif action.lower() == "logout":
                    print("\nOk, logging out..\n")
                    break
                
                else:
                    print("Make sure you select a valid menu option!")
    
    elif action.lower() == "list users":
        User.listUsers()
    
    elif action.lower() == "quit":
        print("Thanks for using our username system!")
        break
    
    else:
        print("Make sure you enter a valid menu choice!")
        