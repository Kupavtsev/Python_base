class Atr_calc():
    def __init__(self, day_open, atr):
        self.day_open = day_open
        self.atr = atr
    
    # Метод задающий 1/2 и Полное движение актива по ATR
    def calc_levels(self):
        self.plus_12 = self.day_open + self.atr * 0.5
        self.plus_F = self.day_open + self.atr
        
    def print_result(self):
        print('The levels is 1/2 = {} and F = {}'.format(self.plus_12, self.plus_F))
        
class Atr_calc_minus(Atr_calc):
    def calc_levels(self):
        self.plus_14 = self.day_open + self.atr * 0.25
        self.plus_34 = self.day_open + self.atr * 0.75
    
    def print_result(self):
        super().print_result()
        print('The levels is 1/4 = {} and 3/4 = {}'.format(self.plus_14, self.plus_34))


day_open, atr = 66164, 178

Atr_calc.value = 18000

test = Atr_calc(day_open, atr)
#test.calc_levels()
#test.print_result()

print(test.value)

#test1 = Atr_calc_minus(day_open, atr)
#test1.calc_levels()
#test1.print_result()

#print(test1.plus_14)
