def hello(name):
    print("Hello, ", name)
hello("John")

#####

x = 2
y = 4
def max2(x,y):
    if x > y:
        return x
    return y

print(max2)

########

def hello_separeted(name = "World", separator = "-"):
    print("Hello", name, sep = separator)                   #sep это какой-то разделитель

hello_separeted("John", "***")
hello_separeted(separator="***", name = "John")