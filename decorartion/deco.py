def my_decorator(func):
    print("裝飾器加點料")
    return func

def my_func():
    print("被裝飾函示執行")

my_func = my_decorator(my_func)

my_func()


# 裝飾函數
def printHello1(func):  # 傳遞需要被裝飾的函數
    def wrapper():
        print("Hello", end=" ")
        return func()
    return wrapper  # 回傳內部函數


@printHello1
def printWorld1():
    print("World")


@printHello1
def printAll1():
    print("everyone!")


printWorld1()
printAll1()


def printHello2(func):
    def wrapper(arg):
        print("Hello", end=" ")
        return func(arg)
    return wrapper


@printHello2
def printWorld2(arg):
    print("World", arg)

@printHello2
def printq(arg=""):
    print("q")


printWorld2("Arvin")
printq("")

# * <-- 一維陣列
# ** <-- 二維陣列


def printHello3(func):
    def wrapper(*args, **kwargs):
        print("Hello", end=" ")
        return func(*args, **kwargs)
    return wrapper


@printHello3
def printSingle(arg):
    print(arg)


@printHello3
def printDouble(arg1, arg2):
    print(arg1, end=" ")
    print(arg2)


@printHello3
def printTriple(arg1, arg2, arg3):
    print(arg1, end=" ")
    print(arg2, end=" ")
    print(arg3)


@printHello3
def printMany(*args):

    for i in args:
        print(i, end=" ")
    print()


@printHello3
def printq3():
    print("q")


printSingle("World")
printDouble("Kitty", "Danny")
printTriple("Kitty", "Danny", "Arvin")
printMany(1, 2, 3, 4)
printq3()
