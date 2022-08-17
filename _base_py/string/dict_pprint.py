import pprint
message = 'Hello new company and welcome !'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# pprint.pprint(count)



# 2nd

message2 = 'Hello new company and welcome !'
count2 = {}
total = {'total': len(message2)}

for character in message2:
    count.setdefault(character, 0)
    count[character] = count[character] + 1


    
# ?pprint.pprint(count)
print(count2, total)
