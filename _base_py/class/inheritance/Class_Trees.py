class Tree(object):
    def __init__(self, kind, height):
         self.kind = kind
         self.age = 0
         self.height = height

    def info(self):
         """ Метод вывода информации о дереве """
         print ("{} years old {}. {} meters high.".format(self.age, self.kind, self.height))    
 
    def grow(self):
        """ Метод роста """
        self.age += 1
        self.height += 0.5

tree_1 = Tree("oak", 0.5)
tree_1.info()
tree_1.grow()
tree_1.info()

class FruitTree(Tree):
    def __init__(self, kind, height):
        # Необходимо вызвать метод инициализации родителя.
        # В Python 3.x это делается при помощи функции super()
        super().__init__(kind, height)
 
    def give_fruits(self):
        print ("Collected 20kg of {}s".format(self.kind))
        
tree_2 = FruitTree("apple", 0.7)
# у нас есть доступ к методам родителя
tree_2.info()
tree_2.grow()
# Мы можем использовать свой метод
tree_2.give_fruits()
# А для родительского экземпляра метод give_fruits() недоступен
tree_1.give_fruits() # Вызовет ошибку
