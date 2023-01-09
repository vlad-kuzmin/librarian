from datetime import datetime
from book import Book


class ReaderBook:

	def __init__(self):
		self.name = None
		self.surname = None
		self.patronymic = None
		self.loving_genre = None
		self.accounting = list()

	def __str__(self):
		personal_data = f"reader book: {self.surname} {self.name}"
		return personal_data

	def add_get_note(self, book: Book, date: datetime):
		self.accounting.append({"book": book, "get_date": date, "pass_date": None})

	def add_pass_note(self, book_name: str, book_author: str, date):
		for note in self.accounting:
			if note["book"].name == book_name and note["book"].author == book_author:
				note["pass_date"] = date

	def get_undelivered_books(self):
		undelivered = list()
		for note in self.accounting:
			if note[2] is None:
				undelivered.append(note)

		return undelivered
