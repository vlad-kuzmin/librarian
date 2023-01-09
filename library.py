from book import Book
from catalog import Catalog
from archive import Archive


class Library:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            raise Exception("У данного класса может быть только один экземпляр")

    def __init__(self, name="unnamed"):
        self.name = name
        self.catalogs = list()
        self.archive = Archive()

    def __str__(self):
        return self.name

    def add_catalog(self, catalog: Catalog):
        self.catalogs.append(catalog)

    def add_book(self, book: Book, amount: int = 1):
        added = False
        for catalog in self.catalogs:
            if catalog.genre == book.genre:
                catalog.add(book, amount)
                added = True
        if not added:
            new_catalog = Catalog(book.genre)
            new_catalog.add(book, amount)
            self.catalogs.append(new_catalog)
