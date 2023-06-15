'''
class Students:
	def __init__(self, name, age):
		self.name = name
		self.age = age

student1 = Students("Fred", 17)
student2 = Students("Mike", 12)
print(student1.name)	# Fred

# Добавление свойств к экземпляру Класса
setattr(student1, 'grade', '8th')
print(student1.grade)	# 8th

hasattr(student1, "grade") #True
'''

# 2
class Empty():
	def __getattr__(self, attrname):
		if attrname == 'age':
			return 40
		else:
			raise AttributeError

# ins_empty = Empty()
# print(ins_empty.name)

# 3
class Accesscontrol:
	def __setattr__(self, attr, value: any) -> None:
		if attr == 'age':
			self.__dict__[attr] = value
		else:
			raise AttributeError

X = Accesscontrol()
X.age = 30
print(X.age)
X.name = 'mel'