import sys


t = lambda x: [sys.stdout.write(line) for line in x]


t(('hello\n', 'there\n'))
