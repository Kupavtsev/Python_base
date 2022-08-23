'''
That is doesn't work with targets exeeded range of list
'''

def recursion_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        middle = len(list)//2

    
    try:
        print('list len: ', len(list))
        while len(list) > middle:
            print('middle: ', list[middle])
            # print('while: ', middle)
            if target == list[middle]:
                return True
            elif target < list[middle]:
                print('start when target < middle: ', list[:middle])
                return recursion_binary_search(list[:middle], target)
            else:
                # print('start when target > middle')
                print('start when target > middle: ', list[middle:])
                return recursion_binary_search(list[middle:], target)
        return False
    except:
        print('The target is out of range')


def verify_result(result):
    print('\nThe result of serching is: ', result, '\n')

list = [1,2,3,4,5,6,7,8,9,10]
# print(list[10])
print(len(list))
target = 15

result = recursion_binary_search(list, target)
verify_result(result)