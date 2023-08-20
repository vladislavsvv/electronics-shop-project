from src.item import Item

class Mixin:
    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self

class Keyboard(Item, Mixin):
    
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Mixin.__init__(self)

    @property
    def language(self):
        return self._language


