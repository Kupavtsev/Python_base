class Students:
	def __init__(self, name, age):
		self.name = name
		self.age = age

student1 = Students("Fred",17)
student1 = Students("Mike",12)

setattr(student1, 'grade', '8th')

hasattr(student1, "grade")      #True
