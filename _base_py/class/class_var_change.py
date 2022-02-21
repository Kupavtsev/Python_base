# Изменяем атрибут Класса через экземпляр Класса
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
print(parent.counter)	# 10
parent.parentFunc()
parent.setCounter(5)	# 5
parent.showCounter()	# 5
parent.setCounter(25)	# 25
parent.showCounter()	# 25