import pytest

from src.item import Item, InstantiateCSVError

"""Здесь надо написать тесты с использованием pytest для модуля item."""

test_item1 = Item('смартфон', 2000, 3)

def test_calculate_total_price():
    assert test_item1.name == 'смартфон'
    assert test_item1.price == 2000
    assert test_item1.quantity == 3
    assert test_item1.calculate_total_price() == 6000
    test_item1.apply_discount()
    assert test_item1.price != 1600


def test_string_to_number():
    assert test_item1.string_to_number("5") == 5
    assert test_item1.string_to_number("7.0") == 7
    assert test_item1.string_to_number("8.5") == 8

def test_str_method():
    assert str(test_item1) == 'смартфон'

def test_repr_method():
    assert repr(test_item1) == "Item('смартфон', 2000, 3)"

def test_instantiate_from_csv():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
