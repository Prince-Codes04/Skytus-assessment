class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

radius = float(input("Enter Radius: "))

circle = Circle(radius)

print("\nCircle Details")
print("Area =", circle.area())
print("Circumference =", circle.circumference())