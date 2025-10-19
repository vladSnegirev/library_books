from books import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def get_all_books(self):
        return [book.get_info() for book in self.books]
