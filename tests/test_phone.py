from src.item import Item
from src.phone import Phone

"""Здесь надо написать тесты с использованием pytest для модуля phone."""

test_item1 = Item('смартфон', 2000, 3)
phone1 = Phone("iPhone 14", 120_000, 5, 2)

def test_class_phone():
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2
    assert test_item1 + phone1 == 8
    assert phone1 + phone1 == 10
    assert test_item1 + 100 == ValueError("Складывать можно только объекты Item и дочерние от них.")
    phone1.number_of_sim = 0
    assert phone1.numer_sim == ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")