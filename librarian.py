class Librarian:
    __instance = None
    __instance_amount = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None or cls.__instance_amount < 3:
            cls.__instance = super().__new__(cls)
            cls.__instance_amount += 1
            return cls.__instance
        else:
            raise Exception("У данного класса может быть только 3 экземпляра")

    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def __str__(self):
        personal_data = f"name: {self.name}\n" \
                        f"surname: {self.surname}\n" \
                        f"patronymic: {self.patronymic}"
        return personal_data
