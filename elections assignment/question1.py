def count():
    string = input("Enter any string: ")
    b = string.count("b")
    a = string.count("a")

    if b == a:
        return print(True)
    else:
        return print(False)


count()
