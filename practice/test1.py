def gen(n):
    for i in n:
        yield i*2



if __name__ == '__main__':
    # n = int(input().strip())
    n = [2,4,6]
    test = gen(n)
    print(list(test))

