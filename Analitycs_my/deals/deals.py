# Deals Quik 06.02.2020

title = '	Цена	Кол-во	Операция	Время	Инструмент'
o1 = '3	63 477	4	Продажа	15:58:56	SiH0 [ФОРТС фьючерсы]'
#c1 = '4	63 455	1	Купля	16:01:52	SiH0 [ФОРТС фьючерсы]'
c1 = '5	63 455	3	Купля	16:01:52	SiH0 [ФОРТС фьючерсы]'

o2 = '6	63 439	3	Купля	16:47:02	SiH0 [ФОРТС фьючерсы]'
#o21 = '7	63 439	1	Купля	16:47:02	SiH0 [ФОРТС фьючерсы]'
c2 = '8	63 444	4	Продажа	16:47:43	SiH0 [ФОРТС фьючерсы]'
'''
9	63 506	1	Продажа	16:58:02	SiH0 [ФОРТС фьючерсы]
10	63 506	3	Продажа	16:58:02	SiH0 [ФОРТС фьючерсы]
11	63 484	4	Купля	16:58:51	SiH0 [ФОРТС фьючерсы]

12	63 502	4	Продажа	17:03:16	SiH0 [ФОРТС фьючерсы]
13	63 480	4	Купля	17:04:02	SiH0 [ФОРТС фьючерсы]

14	63 503	4	Продажа	17:11:04	SiH0 [ФОРТС фьючерсы]
15	63 481	4	Купля	17:11:46	SiH0 [ФОРТС фьючерсы]

16	63 691	4	Купля	17:52:27	SiH0 [ФОРТС фьючерсы]
17	63 674	4	Продажа	17:54:59	SiH0 [ФОРТС фьючерсы]

18	63 696	3	Продажа	18:15:38	SiH0 [ФОРТС фьючерсы]
19	63 696	1	Продажа	18:15:38	SiH0 [ФОРТС фьючерсы]
20	63 674	1	Купля	18:20:22	SiH0 [ФОРТС фьючерсы]
21	63 674	1	Купля	18:20:22	SiH0 [ФОРТС фьючерсы]
22	63 674	1	Купля	18:20:22	SiH0 [ФОРТС фьючерсы]
23	63 674	1	Купля	18:20:22	SiH0 [ФОРТС фьючерсы]
'''


def format_price(price):
    price = price[2:8]
    price = price[0:2] + price[3:]
    return int(price)

def format_side(side):
    if 'Купля' in side:
        side = 'bought'
    else:
        side = 'sold'
    return side

def deal_result(side, enter, cover):
    if side == 'sold':
        result = enter - cover
        return result
    else:
        result = cover - enter
        return result

def format_time(open_time, close_time):
    open_time = open_time[19:28]
    print(open_time)
    close_time = close_time[17:28]
    #time_in_positon = close_time - open_time
    return (open_time, close_time)

def size_position(size):
    size = size[9:11]
    return int(size)

def rubble(size, result):
    rub = size*result - size*2
    return rub

#1
first_open_side = format_side(o1)
first_open_price = format_price(o1)
first_close_price = format_price(c1)

first_result = deal_result(first_open_side, first_open_price, first_close_price)
first_time_in_posiotion = format_time(o1, c1)
first_size = size_position(o1)
first_rubble = rubble(first_size, first_result)


print(type(first_rubble), first_rubble)

#print(first_open_side, type(first_open_side))
#print(first_open_price - first_close_price)

#2
second_open_price = format_price(o2)
second_close_price = format_price(c2)
second_open_side = format_side(o2)

second_result = deal_result(second_open_side, second_open_price, second_close_price)


#print(second_open_price, second_close_price)