class Students:
	def __init__(self, name, age):
		self.name = name
		self.age = age

student1 = Students("Fred", 17)
student2 = Students("Mike", 12)
print(student1.name)

# Добавление свойств к экземпляру Класса
setattr(student1, 'grade', '8th')
print(student1.grade)

hasattr(student1, "grade") 
#True
