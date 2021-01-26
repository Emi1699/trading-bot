from datetime import datetime

class Today():
	def __init__(self):
		pass

	def datetime(self):
		return datetime.today().strftime('%Y-%m-%d %H:%M:%S')