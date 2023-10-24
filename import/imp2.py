from imp import print1
from python1 import thousandDollar

def print2():
    print('Call "print1()" from imp.py')
    print1()
    print("I love dogs!")

if __name__ == '__main__':
    print2()
    k = thousandDollar()
    k.show_num()