from datetime import datetime
from item import Item
# import json_operations
import json
class Receipt():
    def __init__(self):
        self._items = []
        self._date = datetime
        self._category = ""
        self._id = "" # receipt id ?? do we want this to correspond to user id?
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
    def setID(self):
        self._id = 1
    def calculateTotal(self):
        total = 0
        for i in self._items:
            total += i._price
        return total



    def viewReceipt(self):
        string = ""
        string += ("ID: %s\n" %self._id)
        string += ("Store: %s \n" %self._store)
        string += ("Date: %s\n" %self._date)
        string += ("Category: %s\n" %self._category)
        for i in self._items:
            string += ("Name: " + str(i._name) + "," + " Quantity: " + str(i._quantity) + "," + " Price: " + str(i._price))
        return string

    @property
    def category(self):
        return self._category

# r = Receipt()
# r.createReceipt('sample2.json')
