def showNumber(func):
    def number():
        print("123123", end=" ")
        return func()
    return number


@showNumber
def showName():
    print("John")

showName()