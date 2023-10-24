import math

class Point:
    x = 0.0
    y = 0.0
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y
    def showx(self):
        print("x=",float(self.x))
        return
    def showy(self):
        print("y=",float(self.y))
        return

class circle(Point):
    radium = 0.0
    def __init__(self,x=0.0,y=0.0,radium=0.0):
        super().__init__(x,y)
        self.radium = radium
    def showr(self):
        print("radium=",float(self.radium))
    def showarea(self):
        area = self.radium**2*math.pi
        print("area=",float(area))
        return


print("a :")
a = circle(x=3,radium=5)
a.showx()
a.showy()
a.showr()
a.showarea()

print("b :")
b = circle(y=2,radium=2)
b.showx()
b.showy()
b.showr()
b.showarea()

print("c :")
c = circle(2.8,3.5,4)
c.showx()
c.showy()
c.showr()
c.showarea()