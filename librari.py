class Library:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            raise Exception("У данного класса может быть только один экземпляр")

    def __init__(self, name=None):
        self.name = name
        self.books = 0

    def __str__(self):
        return self.name if self.name else "unnamed"
