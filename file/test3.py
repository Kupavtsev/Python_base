def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        f.write(content)

write_to_file('new.txt', 'Some\nnice stock')
write_to_file('existing.txt', 'New line\n', mode='a')


def read_file(filename):
    print('reading file with way_better()')
    with open(filename) as f:
        return f.read()

print(read_file('new.txt'))
print(read_file('existing.txt')) 
