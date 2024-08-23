class Book:
    def __init__(self, title, author):
      self.title = title
      self.author = author
      self.available = True

    def checkout(self):
        if self.available:
          self.available = False
          return True
        else:
          return False
  
    def return_book(self):
      self.available = True
  
    def display_info(self):
      print(f"Title: {self.title}\nAuthor: {self.author}\nAvailable: {'Yes' if self.available else 'No'}")

class Library:
    def __init__(self):
      self.books = []
  
    def add_book(self, book):
      self.books.append(book)
  
    def display_books(self):
      for book in self.books:
        book.display_info()
  
    def get_book_by_title(self, title):
      for book in self.books:
        if book.title.lower() == title.lower():
          return book
      return None

book1 = Book("The Bat", "Jo Nesbo")
book2 = Book("C++", "Deitel")
book3 = Book("AI", "Tselikis")


library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()
