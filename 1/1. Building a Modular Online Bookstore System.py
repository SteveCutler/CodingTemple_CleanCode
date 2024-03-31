# Objective:
# The objective of this assignment is to create a modular online bookstore system using Python. 
# The focus will be on applying the principle of modularity to enhance code organization, maintainability, 
# and scalability. The system will be broken down into different modules, each handling specific 
# functionalities of the bookstore.

# Task 1: Designing the Book Module

# Create a module for managing book-related functionalities. This includes classes and functions 
# for book attributes, book availability, and any other book-specific operations.

# Problem Statement:

# The bookstore system requires a dedicated module for handling various aspects related to books, 
# such as title, author, price, and stock status.

# Code Example:

# book.py

# class Book:
#     # Define book attributes and methods
#     pass
import book

book1984 = book.Book("1984", "George Orwell", 15, "available")

book1984.getAuthor()
book1984.getTitle()
book1984.getPrice()
book1984.getStatus()


# Expected Outcome:

# A well-structured book.py module with a Book class and other necessary functions, focusing 
# on clear, concise, and modular code.

# Task 2: Creating the User Management Module

# Develop a module dedicated to user management, including user registration, login, and profile management.

# Problem Statement:

# The online bookstore needs to manage its users effectively, requiring a separate module for 
# user-related functionalities.

# Code Example:




# # Additional functions for user management

# Expected Outcome:

# A user.py module with a User class and related functions, showcasing the application of 
# modularity in handling user management.

# Task 3: Implementing the Shopping Cart Module

# Create a module for the shopping cart, handling adding books to the cart, viewing the cart, 
# and checkout processes.

# Problem Statement:

# The bookstore system needs a functional and efficient shopping cart system, managed 
# through a separate module.

# Code Example:


# cart.py

# class ShoppingCart:
#     # Define shopping cart attributes and methods
#     pass

# # Additional functions for cart operations

# Expected Outcome:

# A cart.py module with a ShoppingCart class and supplementary functions, demonstrating 
# the use of modularity for efficient shopping cart management.

# Task 4: Integrating the Modules

# Integrate all the created modules (book.py, user.py, cart.py) into a main application 
# module. Ensure seamless interaction between the different modules.

# Problem Statement:

# The final step is to bring together all the individual modules into a cohesive and 
# functioning online bookstore system.

# Code Example:

# main.py

# from book import Book
# from user import User
# from cart import ShoppingCart
# # Code to integrate and utilize the modules

# Expected Outcome:

# A main.py module that effectively integrates the book, user, and cart modules, 
# allowing for a smooth and modular operation of the online bookstore system. 
# The integration should highlight the benefits of modularity in software design.