# Page 564
res = []
for x in range(5):
    if x % 2 == 0:  # Какие значение делятся без остатка
        for y in range(5):
            if y % 2 == 1:  # Какие делятся с остатком
                res.append((x, y))  # Добавить в список в виде картежей

print(res)
# [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]