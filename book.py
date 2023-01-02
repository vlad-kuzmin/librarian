class Book:

	def __init__(self, name: str, author: str, genre: str):
		self.name = name
		self.author = author
		self.genre = genre

	def __str__(self):
		info = f"name: {self.name}\n" \
			   f"author: {self.author}\n" \
			   f"genre: {self.genre}"

		return info
