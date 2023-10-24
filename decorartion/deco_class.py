class d1:
    v1 = 0 
    def __init__(self):
        self.v1 = 0

    def give(self, func):
        def wrapper(arg):
            print("Give money to ", end="")
            return func(arg)
        return wrapper
        