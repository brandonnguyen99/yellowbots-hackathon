from datetime import datetime
from item import Item
# import json_operations
import json
class Receipt():
    def __init__(self):
        self._items = []
        self._name = ""
        self._date = datetime
        self._category = ""
        self._id = ""
        self._store = ""

    def createReceipt(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
            self._store = data.get("store")
            self._date = datetime.strptime(data.get("date"), '%b %d %Y')

            self._category = data.get("category")
            tempItems = data.get("items")
            for it in tempItems:
                new = Item(it.get("name"), it.get("quantity"), it.get("price"), self._store)
                self._items.append(new)
                # print(new)


# r = Receipt()
# r.createReceipt('sample2.json')
