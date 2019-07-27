from user import User
from receipt import Receipt

class System():
    def __init__(self):
        self._user = []

    def add_user(self, user):
        self._user.append(user)

    def user_receipt(self, filename, id):
        new = Receipt()
        new.createReceipt(filename)
        for u in self._user:
            if id == u.id:
                u.addReceipt(new)
# s = System()
# u = User(1)
# s.add_user(u)
# s.user_receipt('sample.json', 1)
