import json

class OHLC(object):
    def __init__(self, date, day_open, high, low, close):
        self.stock = 'BA'
        self.date = date
        self.day_open = day_open
        self.high = high
        self.low = low
        self.close = close


one = OHLC(40, 40.50, 39.50, 40.25)
two = OHLC(40.25, 40.75, 40, 40.50)

change = two.close - one.close
change_percent = change / one.close * 100

print(change)
print(round(change_percent, 2),'%')

data = {'Stock': one.stock, 'Change': change, '% Change': change_percent}
print(data)