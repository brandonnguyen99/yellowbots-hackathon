from datetime import datetime
from item import Item
# import json_operations
import json
class Receipt():
    def __init__(self):
        self._items = []
        self._date = datetime
        self._category = ""
        self._id = 0 # receipt id ?? do we want this to correspond to user id?
        self._store = ""
        self._img=""
        self._fromjson=""

    def createReceipt(self, file):
        self._fromjson = file
        with open(file, 'r') as f:
            data = json.load(f)
            self._store = data.get("store")
            self._date = datetime.strptime(data.get("date"), '%b %d %Y').date()
            self._img = data.get("img")
            self._category = data.get("category")
            self._id = data.get("id")
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

    def calculateTotal(self):
        cost = 0
        for item in self._items:
            cost = cost + item.price
        return cost

    @property
    def category(self):
        return self._category

    @property
    def store(self):
        return self._store

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def img(self):
        return self._img

    @property
    def fromjson(self):
        return self._fromjson

# r = Receipt()
# r.createReceipt('sample2.json')
