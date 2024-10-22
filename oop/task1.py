
class Book:
    def __init__(self, name, author, year, genre, pages):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []
         
    def add_book(self, book: Book):
        self.books.append(book)

    def search_by_title(self, title):
        for book in self.books:
            if book.name == title:
                return book
            else:
                return "Did not find your favourite book"
            
    def delete_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
        else:
            return "Your book is not in library"


    def get_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def get_books_sorted_by_year(self):
        return sorted(self.books, key=lambda book: book.year)

# Пример использования
library = Library()
book1 = Book("Название1", "Автор1", 2001, "Жанр1", 300)
book2 = Book("Название2", "Автор2", 1999, "Жанр2", 150)
book3 = Book("Название3", "Автор3", 1999, "Жанр3", 150)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.delete_book(book3)
print(library.search_by_title("Название1"))
print(library.get_books_by_author("Автор1"))
print(library.get_books_sorted_by_year())
