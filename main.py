from interface import LibraryClientInterface
from library import Library
from librarian import Librarian

if __name__ == "__main__":
	print("Приложение для работы библиотеки v 0.0.1 DemoVersion")
	print("Для того что бы взять книгу из библиотеки введите команду lend")
	print("Для того что бы вернуть книгу введите команду return")
	library = Library("Библиотека Конгресса")
	librarian = Librarian("Дональд", "Трамп", "Джон")
	librarian.set_library(library)
	librarian.add_book("1984", "Джордж Оруэл", "Роман", 10)
	librarian.add_book("Стихи", "Александр Пушкин", "Поэзия", 5)
	client_interface = LibraryClientInterface(library, librarian)
	while True:
		console = input("Введите команду: ")
		if console == "lend":
			client_interface.lend_book()
		elif console == "return":
			client_interface.return_book()
