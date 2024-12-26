class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                self.borrowed_books[book_id] = book
                return book
        raise ValueError("Book not available")

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            book = self.borrowed_books.pop(book_id)
            self.books.append(book)
        else:
            raise ValueError("Book not borrowed")

    def view_books(self):
        return self.books
