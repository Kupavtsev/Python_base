# Файл updatedb.py: обновляет объект класса Person в базе данных

import shelve
db = shelve.open('D:\Dropbox\it\Python\Python_Examples\examples\db\person\persondb')

for key in db:
    print(key, '\t=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue
#print(sue)

db.close()