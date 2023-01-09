from library import Library
from librarian import Librarian
from prettytable import PrettyTable


class LibraryClientInterface:

	__instance = None

	def __new__(cls, *args, **kwargs):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			raise Exception("У данного класса может быть только один экземпляр")

	def __init__(self, library: Library, librarian: Librarian | None = None):
		self.__library = library
		self.__librarian = librarian

	def lend_book(self):
		book_name = input("Введите название книги: ")
		book_author = input("Введите автора книги: ")
		book_genre = input("Введите жанр: ")
		book_name = book_name if book_name else None
		book_author = book_author if book_author else None
		book_genre = book_genre if book_genre else None

		searched = list(set(self.__librarian.search_book(
			book_name,
			book_author,
			book_genre
		)))
		searched_table = PrettyTable()
		searched_table.title = "НАЙДЕННЫЕ КНИГИ"
		searched_table.field_names = ["Книга", "Номер"]
		for book_num in range(len(searched)):
			searched_table.add_row([searched[book_num], book_num + 1])

		print(searched_table)

		while True:
			try:
				book_num = int(input("Введите номер книги: "))
				break
			except ValueError:
				print("Вы ввели не число. Попробуйте еще раз.")

		print("Для того что бы взять книгу введите свои данные.")
		name = input("Введите имя: ")
		surname = input("Введите фамилию: ")
		patronymic = input("Введите отчество: ")
		self.__librarian.register_reader(name, surname, patronymic)
		self.__librarian.add_get_note_to_reader_book(searched[book_num - 1], name, surname, patronymic)
		self.__librarian.del_book(searched[book_num - 1])

	def return_book(self):
		name = input("Введите имя: ")
		surname = input("Введите фамилию: ")
		patronymic = input("Введите отчество: ")
		book_name = input("Введите название книги: ")
		book_author = input("Введите автора книги: ")
		book_genre = input("Введите жанр: ")
		self.__librarian.add_pass_note_to_reader_book(name, surname, patronymic, book_name, book_author)
		self.__librarian.add_book(book_name, book_author, book_genre)
