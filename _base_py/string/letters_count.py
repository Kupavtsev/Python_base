import pprint
message = 'Hello new company and welcome !'
count = {}
total = {'total': len(message)}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1


    
# ?pprint.pprint(count)
print(count, total)
