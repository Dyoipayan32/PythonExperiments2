class Library:
    def __init__(self):
        self.collections = list()

    def display_all_books(self):
        if not self.collections:
            print("Library is empty. No book is added.")
        for eachBook in self.collections:
            print(eachBook)

    def add_a_book(self, book):
        self.collections.append(book)
        print("Book >> {} , is added to the library.".format(book))

    def find_a_book_by_title(self, title):
        for book_ in self.collections:
            if title.lower() in book_.getTitle().lower():
                print("Book is found in the library.")
                print("Book name: {}. ".format(book_.getTitle()))
                print("Book author: {}. ".format(book_.getAuthorName()))


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{} by, {}".format(self.title, self.author)

    def getTitle(self):
        return self.title

    def getAuthorName(self):
        return self.author


lib = Library()
lib.display_all_books()
book_ = Book("The Treasures Trove", "D.P Bhattacharya")
lib.add_a_book(book_)
lib.display_all_books()
lib.find_a_book_by_title("Treasures")
print("------------------------------\n")
book__ = Book("Let us C", "Yashavant Kanetkar")
lib.add_a_book(book__)
lib.display_all_books()
lib.find_a_book_by_title("C")

