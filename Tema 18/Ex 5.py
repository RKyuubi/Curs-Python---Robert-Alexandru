class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} - {self.author}'

class Ebook(Book):
    def __init__(self, title, author, file_size, ebook_format):
        super().__init__(title, author)
        self.file_size = file_size
        self.ebook_format = ebook_format

    def __str__(self):
        return f'{self.title} - {self.author} / {self.ebook_format} - {self.file_size} MB'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print (f"Cartea '{book.title}' a fost adaugata in biblioteca")

    def list_books(self):
        if not self.books:
            print ("Biblioteca este goala")
        else:
            for book in self.books:
                print(book)

    def ebook_space(self):
        total_size = 0
        for book in self.books:
            if isinstance(book, Ebook):
                total_size += book.file_size
        return total_size

if __name__ == "__main__":
    library = Library()

    book1 = Book("A Brief History of Time", "Stephen Hawking")
    ebook1 = Ebook("Dune", "Frank Herbert", 10, "PDF")
    ebook2 = Ebook("Harry Potter", "J.K.Rowling", 12, "PDF")
    book2 = Book("Jungle Book", "Rudyard Kipling")


    library.add_book(book1)
    library.add_book(book2)
    library.add_book(ebook1)
    library.add_book(ebook2)
    print ()
    print("--Books and Ebooks--")
    library.list_books()
    print ()
    total_space = library.ebook_space()
    print (f"Spatiul total ocupat de Ebooks este: {total_space} MB")