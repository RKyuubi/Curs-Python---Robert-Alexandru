class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_type(self):
        if self.pages > 150:
            print("Cartea este roman")
        else:
            print("Cartea este nuvela")

if __name__ == "__main__":
    carte = Book("Fram, ursul polar", "Cezar Petrescu", 155)
    carte.book_type()