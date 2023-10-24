from deco_class import d1

d2 = d1()
    

@d2.give
def printName(arg):
    print(arg)


printName("Kitty")
