from user import User
from receipt import Receipt
from data import Data

class System():
    def __init__(self):
        self._user = []
        self._receipts = []

    def add_users(self):
        d = Data()
        self._user = d.makeUsers()

    def user_receipt(self, filename, id):
        new = Receipt()
        new.createReceipt(filename)
        found = False
        for u in self._user:
            if id == u.id:
                u.addReceipt(new)
                self._receipts.append(new)
                found = True
        return found
    def generateID(self):
        id = 0
        for r in self._receipts:
            if r._id > id:
                id = r._id
        id = id + 1
        return id
    def getCategories(self):
        categories = []
        if len(self._receipts) == 0:
            # categories.append("test")
            return categories
        categories.append("all")
        for r in self._receipts:
            if r._category not in categories:
                categories.append(r._category)
        return catergories
    @property
    def user(self):
        return self._user

            # print error- output to front end
# s = System()
# s.add_users()
# # u = User(1,"p_1")
# s.user_receipt('sample.json', 1)
