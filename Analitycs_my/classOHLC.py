import json
from datetime import datetime

# today = datetime.today()
# print(today)
# datem = datetime(2021, 1, 6)
# print(datem)

class OHLC(object):
    def __init__(self, date, day_open, high, low, close):
        self.stock = 'BA'
        self.date = date
        self.day_open = day_open
        self.high = high
        self.low = low
        self.close = close

one_date = datetime(2021, 1, 6)
one = OHLC(one_date, 40, 40.50, 39.50, 40.25)
two_date = datetime(2021, 1, 7)
two = OHLC(two_date, 40.25, 40.75, 40, 40.50)

change = two.close - one.close
change_percent = change / one.close * 100

print(two.date)
print(round(change_percent, 2),'%')

data = {'Stock': one.stock, 'Change': change, 'Change %': round(change_percent, 2)}
print(data)