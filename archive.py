from reader_book import ReaderBook


class Archive:

	def __init__(self):
		self.__archive = list()

	def add(self, reader_book: ReaderBook):
		self.__archive.append(reader_book)

	def search_by_personal_data(self, name: str, surname: str, patronymic: str):
		for reader_book in self.__archive:
			if reader_book.name == name and reader_book.surname == surname and reader_book.patronymic == patronymic:
				return reader_book
