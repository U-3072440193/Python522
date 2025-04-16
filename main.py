class Book:
    def __init__(self, title, autor, status):
        self.title = title
        self.autor = autor
        self.status = status



class Library(Book):
    def add_book(self,title,autor, status=1):
