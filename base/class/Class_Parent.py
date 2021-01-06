class Parent:
	counter = 10
	def __init__(self):
		print("Class initialized")
	def parentFunc(self):
		print("ParentFunc being called")
	def setCounter(self, num):
		Parent.counter = num
		print(num)
	def showCounter(self):
		print(str(Parent.counter))

parent = Parent()
parent.parentFunc()
parent.setCounter(5)
parent.showCounter()