from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    def __str__(self):
        return self.name

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self._number_of_sim = value