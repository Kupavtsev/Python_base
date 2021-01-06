#5
import pprint

message = 'Hello and welcome!'
count = {}

for c in message:
    count.setdefault(c, 0)
    count[c] = count[c] + 1

pprint.pprint(count)