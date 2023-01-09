from book import Book


class Catalog:

	def __init__(self, genre):
		self.storage = list()
		self.genre = genre

	def add(self, book: Book, amount: int = 1):
		if book.genre == self.genre:
			self.storage.extend([book for _ in range(amount)])
		else:
			print(f"В этот каталог можно добавлять только книги жанра {self.genre}.")

	def search_by_name(self, name):
		search_result = list()

		for book in self.storage:
			if book.name == name:
				search_result.append(book)

		return search_result

	def search_by_author(self, author):
		search_result = list()

		for book in self.storage:
			if book.author == author:
				search_result.append(book)

		return search_result

	def exact_search(self, name, author):
		search_result = list()

		for book in self.storage:
			if book.name == name and book.author == author:
				search_result.append(book)

		return search_result

	def search_and_delete(self, name: str, author: str, amount: int = 1):
		searched_indexes = list()
		for book_ind in range(len(self.storage)):
			if self.storage[book_ind].name == name and self.storage[book_ind].author == author:
				searched_indexes.append(book_ind)
		for i in range(amount):
			self.storage.pop(searched_indexes[i])

	def delete(self, book: Book):
		if book in self.storage:
			self.storage.remove(book)

	def __str__(self):
		info = f"catalog genre: {self.genre}\n" \
			   f"books amount: {len(self.storage)}"

		return info
