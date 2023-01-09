class Book:

	def __init__(self):
		self.name = None
		self.author = None
		self.genre = None

	def __str__(self):
		info = f"Название: {self.name}\n" \
			   f"Автор: {self.author}\n" \
			   f"Жанр: {self.genre}"

		return info
