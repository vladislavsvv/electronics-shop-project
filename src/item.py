import csv

class InstantiateCSVError(Exception):
    pass

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity


        Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return other.quantity + self.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_price_quantity = self.price * self.quantity
        return float(all_price_quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) <= 10:
            self.__name = value
        "Длина наименования товара превышает 10 символов"

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open('../src/items.csv', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'key' not in row or 'key' not in row or 'key' not in row:
                        raise InstantiateCSVError
                    cls.all.append(row)
                return cls
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
        except InstantiateCSVError:
            print(" InstantiateCSVError: Файл item.csv поврежден")


    @staticmethod
    def string_to_number(number):
        f_number = float(number)
        int_number = int(f_number)
        return int_number



