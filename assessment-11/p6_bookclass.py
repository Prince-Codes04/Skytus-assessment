class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("\nBook Details")
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self.price)

title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
price = float(input("Enter Book Price: "))

book = Book(title, author, price)
book.display()