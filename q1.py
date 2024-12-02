# Define a class Book with attributes title and author. Create an object of this class and display the values of the attributes.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create an object of book

Book1 = Book("Harry potter", "F.Scott Fitzgerald")

#Display the values

print("Book Title:", Book1.title)
print("book Author:",Book1.author)