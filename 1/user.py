from cart import ShoppingCart

class User:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = ShoppingCart()

    def registerUser():
        global Users
        print("\nOk lets register a new user...\n")
        username = input("What username would you like to use?\n").strip()
        password = input("What password would you like to use?\n").strip()
        if username not in Users:
            Users[username.lower()] = User(username, password)
            print(f"\nNew user '{username.capitalize()}' registered!")
        else:
            print(f"Sorry! The username '{username.capitalize()}' already exists!")

    def deleteUser():
        global Users
        print("\nOk lets delete your account...")
        user = input("What's the username for your account?").strip().lower()
        if user in Users:
            password = input("What's the password for your account? (case specific)")
            if Users[user].password == password:
                del Users[user] 
                print("Succesfully deleted!")
            else:
                print("Sorry, that password is incorrect!")
        else:
            print("Sorry, I couldn't find that username in our database!")

    def listUsers():
        print("\nOk lets list the registered users:")
        if not Users:
            print("User list empty!")
        for user in Users.keys():
            print({user})
    
    def signIn():
        print("\nOk let's sign you in..\n")
        user = input("What's the username for your account?\n").strip().lower()
        if user in Users:
            password = input("What's the password for your account? (case specific)\n")
            if Users[user].password == password:
                print("\nYou've been succesfully signed in!\n")
                return Users[user]
            else:
                print("\nSorry, that password is incorrect!\n")

        else:
            print("\nSorry, I couldn't find that username in our database!\n")




Users = {}