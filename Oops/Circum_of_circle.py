class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius=radius

    def circ(self):
        return Circle.pi * self.radius*2

my_circle = Circle(radius=200)
print(my_circle.circ())