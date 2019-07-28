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
    def receipts(self):
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
            if (receipt.category == "category"):
                category_receipts.append(receipt)

        return category_receipts
    def retrieveCompany(self, category):
        categoryComp = []
        if category == "all":
            for a in self._receipts:
                if a.store not in categoryComp:
                    categoryComp.append(a.store)
        else :
            for c in self._receipts:
                if c._category == category:
                    categoryComp.append(c.store)

        return categoryComp

    def receiptStore(self, store):
        store_receipts = []
        for r in self._receipts:
            if r._store == store:
                store_receipts.append(r)
        return store_receipts


    def __str__(self):
        return "id: {}, Receipts: {}".format(self._id, self._receipts)
