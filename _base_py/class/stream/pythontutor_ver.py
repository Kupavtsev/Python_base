class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while len(L) < 5:
        # while 1:
            data = self.reader
            if not data: break
            data = self.converter(data)
            self.writer.append(data)
            # self.writer.write(data)
    def converter(self, data):
        assert False, 'converter must be defined'
        
class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

class HTMLize:
    def write(self, line):
        print(f'<PRE>{line.rstrip()}</PRE>')


if __name__ == '__main__':
    # L = ['nyse', 'scalping', 'nasdaq', 'swing']
    S = 'scalping and poker'
    obj = Uppercase(S, L)
    obj.process()

    # html = Uppercase(S, HTMLize())
    # html.process()

    