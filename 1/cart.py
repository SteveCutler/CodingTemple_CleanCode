
class ShoppingCart:

    def __init__(self):
        self.contents = {}

    def addBook(user, book):
        user.cart.contents[book.title] = book

    def removeBook(user, book):
        del user.cart.contents[book.title]

    def listContents(self):
        print("\nLets check which books you have in your cart...\n")
        if self.contents:
            print(list(self.contents.keys()))
        else:
            print("It doesn't look like there's any books in your cart!\n")

    def checkout(cart):
        print("\nOk lets go to the checkout and see what your total is...")
        sum = 0
        for book in cart.contents.values():
            sum += book.price
        print(f"The total cost of all the books in your cart is: ${sum}")
        response = input("\nWould you like to purchase these books? (yes, no)\n").strip().lower()
        if response == "yes":
            print("\n*cha-CHING* Thank you for coming!")
            cart.contents.clear()
            print("\nYour cart is empty!")
        else:
            print("\nOk fine...")
            # add cost of all books up
            # print cost and ask how much money they have
            #     if they have enough, deduct cost from the input money amount, return change, clear cart
            #     if not, say sorry you need {difference} to purchase these books

#Carts = {}