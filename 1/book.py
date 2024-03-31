
class Book:
    Books = {}
    def __init__(self, title, author, price, status):
        self.title = title
        self.author = author
        self.price = price
        self.status = status
        

    def getTitle(self):
        print(self.title)

    def getAuthor(self):
        print(self.author)

    def getPrice(self):
        print(self.price)

    def getStatus(self):
        print(self.status)

    def addBook(title, author, price, status):
        if title not in Book.Books:
            newBook = Book(title, author, price, status)
            Book.Books[title] = newBook
        else:
            print("That book already exists!")

    


