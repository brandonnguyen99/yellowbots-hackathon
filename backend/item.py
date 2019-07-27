class Item():
    def __init__(self, name, quantity, price, store):
        self._name = name # Name of item
        self._quantity = quantity # Quantity of how much you bought
        self._price = price # Price of 1 item
        self._store = store # Store you bought it from

    # Properties
    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self._price

    @property
    def store(self):
        return self._store    
