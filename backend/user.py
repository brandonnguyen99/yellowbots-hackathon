from receipt import Receipt
class User():
    def __init__(self, id, password):
        # password
        self._id = id
        self._receipts = []
        self._password = password

    @property
    def id(self):
        return self._id

    @property
    def total_receipts(self):
        return self._receipts

    @property
    def num_receipts(self):
        return len(self._receipts)

    # @receipts.setter
    def addReceipt(self, newReceipt):
        self._receipts.append(newReceipt)

    def retrieveCategory(self, category):
        category_receipts = []
        for receipt in self._receipts:
            if (receipt.category == category):
                category_receipts.append(receipt)

        return category_receipts
    def retrieveCompany(self, category):
        categoryComp = []
        for c in self._receipts:
            if c._category == category:
                categoryComp.append(c)

        return categoryComp

    def authenticate(id, password):
        if self._id == id and self._password == password:
            return True
        else:
            return False

    def __str__(self):
        return "id: {}, Receipts: {}".format(self._id, self._receipts)
