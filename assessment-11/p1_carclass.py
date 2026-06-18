class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 20

    def brake(self):
        self.speed -= 10

    def display(self):
        print("Car Details")
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Speed :", self.speed, "km/h")
        print()

car = Car("BMW", "M4", 120)

print("Initial Details:")
car.display()

print("After Accelerating:")
car.accelerate()
car.display()

print("After Braking:")
car.brake()
car.display()