from book import Book
from reader_book import ReaderBook


class BookBuilder:

	def __init__(self):
		self.__book = Book()

	def reset(self):
		self.__book = Book()

	def set_name(self, name: str):
		self.__book.name = name

	def set_author(self, author: str):
		self.__book.author = author

	def set_genre(self, genre: str):
		self.__book.genre = genre

	def get_result(self):
		return self.__book


class ReaderBookBuilder:

	def __init__(self):
		self.__reader_book = ReaderBook()

	def reset(self):
		self.__reader_book = ReaderBook()

	def set_name(self, name: str):
		self.__reader_book.name = name

	def set_surname(self, surname: str):
		self.__reader_book.surname = surname

	def set_patronymic(self, patronymic: str):
		self.__reader_book.patronymic = patronymic

	def get_result(self):
		return self.__reader_book
