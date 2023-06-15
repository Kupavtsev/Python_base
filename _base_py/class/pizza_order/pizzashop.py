from time import process_time_ns
from employees import PizzaRobot, Server

class Customer(object):
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, 'orders from', server)
    def pay(self, server):
        print(self.name, 'pays for item to', server)

class Oven:
    def bake(self):
        print('oven bakes')

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')             # Встроить другие объекты
        self.chef = PizzaRobot('Bob')           # Робот по имени Bob
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)               # Активизировать другие объекты
        print(f'Customer created: {customer.name}')
        customer.order(self.server)             # Клиент делает заказ официанту
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    import pickle

    scene = PizzaShop()
    scene.order('Homer')
    print('....')
    scene.order('Marsh')

    pickle.dump(scene, open('scenefile.dat', 'wb'))