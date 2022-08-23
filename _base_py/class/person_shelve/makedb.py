# Файл makedb.py: сохраняет объекты Person в хранилище

from person import Person, Manager

bob = Person('Bob Walsh')
sue = Person('Sue Jones', job='dev', pay=100000)
tom  = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb2')
for object in (bob, sue, tom):
    print(object)
    db[object.name] = object
db.close()