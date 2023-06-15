from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

class HTMLize:
    def write(self, line):
        print(f'<PRE>{line.rstrip()}</PRE>')

if __name__ == '__main__':
    import sys
    obj = Uppercase(open('spam.txt'), sys.stdout)
    obj.process()

    html = Uppercase(open('spam.txt'), HTMLize())
    html.process()