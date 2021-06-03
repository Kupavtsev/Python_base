def hello_separeted(name = "World", separator = "-"):
    print("Hello", name, sep = separator)                   #sep это какой-то разделитель

hello_separeted("John", "***")
hello_separeted(separator="***", name = "John")