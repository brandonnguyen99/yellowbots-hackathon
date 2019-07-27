from user import User
# from system import System

class Data():
    def makeUsers(self):
        list_user = []
        # for i in range(6):
        # password = "p_" + str(i)
        new = User(1, "password")
        list_user.append(new)
        return list_user
