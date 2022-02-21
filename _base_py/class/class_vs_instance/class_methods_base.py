class Worker:
    def __init__(self, name, pay): # Инициализация при создании
        self.name = name           # self – это сам объект
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1] # Взять поледний элемент Массива (фамилию)
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # Обновить сумму выплат
        print(self.pay)
        return self.pay

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
print(bob.lastName())   # Smith

bob.giveRaise(10)       # 55000.0
print(round(bob.pay))   # 55000 