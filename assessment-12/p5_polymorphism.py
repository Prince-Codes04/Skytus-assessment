class Rectangle:
    def area(self):
        return 50

class Circle:
    def area(self):
        return 153.86

def show_area(shape):
    print("Area =", shape.area())

r = Rectangle()
c = Circle()

show_area(r)
show_area(c)