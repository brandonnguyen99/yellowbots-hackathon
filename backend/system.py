from user import User

class System():
	def __init__(self):
		self._user = []

	def add_user(self, user):
		self._user.append(user)

