

class Book:
    """
        The class that represents the Book

        Attributes:
        name (str): the title of the book
        author (str): the author of the book
        year (int): the year of publication
        genre (str): the genre of the book 
        pages (int): The bumner of pages within a book.
    """

    def __init__(self, name, author, year, genre, pages):
        """
            Initializes the book with following parameters:

            Attributes:
            name (str): the title of the book
            author (str): the author of the book
            year (int): the year of publication
            genre (str): the genre of the book 
            pages (int): The bumner of pages within a book. 
        """
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages

    def __str__(self):
        print(f'book has following info: name:{self.name}, author:{self.author}, year:{self.year}, genre:{self.genre}, pages:{self.pages}')


class Library:
    """
        The class that represents the Library

        Attributes:
        books (list): an array of the books
    """
    def __init__(self):
        """
            The method initializes and creates new array of books

            Attributes:
            books (list): an array of the books
        """
        self.books = []
         
    def add_book(self, book: Book):
        """
            The method allows to add new book to the library catalog

            Args:
                book (Book): the book object that needs to be saved in a library
        """
        self.books.append(book)

    def search_by_title(self, title: str = None):
        """
            This method allows to search books based on its title
        """
        for book in self.books:
            if book.name == title:
                return book
            else:
                raise Exception("Book was not found")
            
    def delete_book(self, book: Book = None):
        """
            This method deletes the book

            Args:
                book (Book): The book which must be deleted
            
            Returns:
                Either function returns the message that your book is not in the library or it just removes the book
        """
        if book in self.books:
            self.books.remove(book)
            return "Book successfully deleted"
        else:
            raise Exception("Book was not found")


    def get_books_by_author(self, author: str = None):
        """
            This method finds book based on the authors name

            Args:
                author (str): The book author
            
            Returns:
                book (Book): The available books that were written by this author  
        """
        return [book for book in self.books if book.author == author]

    def get_books_sorted_by_year(self):
        """
            This method finds and sorts books by year

            Args:
                None
            
            Returns:
                array of sorted books by year
        """
        return sorted(self.books, key=lambda book: book.year)


# Пример использования

if __name__ == '__main__':
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
