class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} - {self.author}"

class Library:
    def __init__(self):
        self.book = []

    def add_book(self, book):
        self.book.append(book)

    def find_by_author(self, author):
        return [book for book in self.book if book.author == author]

    def list_books(self):
        for book in self.book:
            print(book)

