class a():
	def __init__(self):
		print("adsasd")
	def __new__(cls):
		print("1235645")
		return object.__new__(cls)
a()

