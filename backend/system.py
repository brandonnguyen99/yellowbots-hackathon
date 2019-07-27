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
                print("test")
                found = True
        return found
    def login(self, id, password):
        for user in self._user:
            if user.authenticate(id, password) == True:
                return user
        return False

            # print error- output to front end
# s = System()
# s.add_users()
# # u = User(1,"p_1")
# s.user_receipt('sample.json', 1)
