# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book
# to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books
class Author:
    def __init__(self, author_name: str, author_country: str, birthday: int, author_books: str = []):
        self.author_name = author_name
        self.author_country = author_country
        self.birthday = birthday
        self.author_books = author_books

    def __repr__(self):
        return f'{self.author_name}'

    def __str__(self):
        return f'{self.author_name}'

class Book:

    def __init__(self, books_name: str, year: int, author: Author):
        self.books_name = books_name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'({self.books_name}, {self.year}, {self.author})'

    def __str__(self):
        return f'({self.books_name}, {self.year}, {self.author})'

class Library:
    sum_books = 0
    def __init__(self, l_name: str, books: str = [], authors = []):
        self.l_name = l_name
        self.books = books
        self.authors = authors

    def __repr__(self):
        return f'{self.l_name}, {self.books}, {self.authors}'

    def __str__(self):
        return f'{self.l_name}, {self.books}, {self.authors}'

    def new_book(self, name: str, year: int, author: Author):
        if not name:
            print("Empty book name")
            return

        temp_book = Book(name, year, author)
        self.books.append(temp_book)

        if not author in self.authors:
            self.authors.append(author)

        self.sum_books += 1

        return temp_book

    def group_by_author(self, author: Author)->list:
        group = []
        for book in self.books:
            if author == book.author:
                group.append(book)
        return group

    def group_by_year(self, year: int)->list:
        group = []
        for book in self.books:
            if year == book.year:
                group.append(book)
        return group


author_1 = Author('Ok', 'USA', 1900)
author_2 = Author('DL', 'UK', 1960)
author_3 = Author('KO', 'Ch', 2000)
l = Library('lib1')
book_1 = l.new_book('Book1', 1946, author_1)
book_2 = l.new_book('Book2', 2000, author_2)
book_3 = l.new_book('Book3', 2010, author_2)
#book_3 = l.new_book('', 1, author_2)
print(l)
print(l.group_by_author(author_2))
print(f'Кількість всіх книг: {l.sum_books}')