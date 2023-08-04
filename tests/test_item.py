from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""

test_item1 = Item('смартфон', 2000, 3)


def test_calculate_total_price():
    assert test_item1.name == 'смартфон'
    assert test_item1.price == 2000
    assert test_item1.quantity == 3
    assert test_item1.calculate_total_price() == 6000
    test_item1.apply_discount()
    assert test_item1.price == 1600
