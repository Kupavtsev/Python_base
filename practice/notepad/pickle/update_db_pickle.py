import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Hardy2'

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()