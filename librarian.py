from library import Library
from builders import BookBuilder
from book import Book
from builders import ReaderBookBuilder
from datetime import datetime


class Librarian:
    __instance = None
    __instance_amount = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None or cls.__instance_amount < 3:
            cls.__instance = super().__new__(cls)
            cls.__instance_amount += 1
            return cls.__instance
        else:
            raise Exception("У данного класса может быть только 3 экземпляра")

    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.__book_builder = BookBuilder()
        self.__reader_book_builder = ReaderBookBuilder()
        self.__library = None

    def __str__(self):
        personal_data = f"name: {self.name}\n" \
                        f"surname: {self.surname}\n" \
                        f"patronymic: {self.patronymic}"
        return personal_data

    def set_library(self, library: Library):
        self.__library = library

    def add_book(self, name: str, author: str, genre: str, amount: int = 1):
        self.__book_builder.reset()
        self.__book_builder.set_name(name)
        self.__book_builder.set_author(author)
        self.__book_builder.set_genre(genre)
        book = self.__book_builder.get_result()
        for _ in range(amount):
            self.__library.add_book(book)

        if amount == 1:
            print(f"Книга добавлена в библиотеку\n"
                  f"{book}")
        else:
            print(f"Тираж в {amount} книг добавлен в библиотеку.\n"
                  "Информация о книге:\n"
                  f"{book}")

    def search_book(self, name: str | None = None, author: str | None = None, genre: str | None = None):
        searched_books = list()
        if name is not None and author is not None and genre is None:
            for catalog in self.__library.catalogs:
                searched = catalog.exact_search(name, author)
                if searched:
                    searched_books.extend(searched)
        elif name is not None and author is None and genre is None:
            for catalog in self.__library.catalogs:
                searched = catalog.search_by_name(name)
                if searched:
                    searched_books.extend(searched)
        elif name is None and author is not None and genre is None:
            for catalog in self.__library.catalogs:
                searched = catalog.search_by_author(author)
                if searched:
                    searched_books.extend(searched)
        elif name is None and author is None and genre is not None:
            for catalog in self.__library.catalogs:
                if catalog.genre == genre:
                    searched_books.extend(catalog.storage)
        elif name is not None and author is None and genre is not None:
            for catalog in self.__library.catalogs:
                if catalog.genre == genre:
                    searched = catalog.search_by_name(name)
                    if searched:
                        searched_books.extend(searched)
        elif name is None and author is not None and genre is not None:
            for catalog in self.__library.catalogs:
                if catalog.genre == genre:
                    searched = catalog.search_by_author(author)
                    if searched:
                        searched_books.extend(searched)
        elif name is not None and author is not None and genre is not None:
            for catalog in self.__library.catalogs:
                if catalog.genre == genre:
                    searched = catalog.exact_search(name, author)
                    searched_books.extend(searched)

        return searched_books

    def search_and_del_book(self, name: str, author: str, genre, amount: int = 1):
        for catalog in self.__library.catalogs:
            if catalog.genre == genre:
                catalog.delete(name, author, amount)

    def del_book(self, book: Book):
        for catalog in self.__library.catalogs:
            if book in catalog.storage:
                catalog.delete(book)
                break

    def register_reader(self, name: str, surname: str, patronymic: str):
        self.__reader_book_builder.reset()
        self.__reader_book_builder.set_name(name)
        self.__reader_book_builder.set_surname(surname)
        self.__reader_book_builder.set_patronymic(patronymic)
        result = self.__reader_book_builder.get_result()
        self.__library.archive.add(result)

    def add_get_note_to_reader_book(self, book: Book, name: str, surname: str, patronymic: str):
        reader_book = self.__library.archive.search_by_personal_data(name, surname, patronymic)
        if reader_book:
            reader_book.add_get_note(book, datetime.now().strftime("%d-%m-%Y"))

    def add_pass_note_to_reader_book(self, name: str, surname: str, patronymic: str, book_name: str, book_author: str):
        reader_book = self.__library.archive.search_by_personal_data(name, surname, patronymic)
        if reader_book:
            reader_book.add_pass_note(book_name, book_author, datetime.now().strftime("%d-%m-%Y"))
