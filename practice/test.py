if __name__ == '__main__':
# n = int(input().strip())

    # for n in range(0,24):
    
    if 1 <= n <= 100:
        if n % 2 != 0:
            print(n, 'Weird')
        # elif 2 <= n <= 5:
        #     print('Not Weird')
        # elif 6 <= n <= 20:
        #     print('Weird')
        elif n in range(2, 6):
            print(n, 'Not Weird')
        elif n in range(6, 21):
            print(n, 'Weird')
        elif n > 20:
            print(n, 'Not Weird')
    else:
        pass