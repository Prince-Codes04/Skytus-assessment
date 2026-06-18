class Vehicle:
    def show_vehicle(self):
        print("This is a Vehicle")

class Car(Vehicle):
    def show_car(self):
        print("This is a Car")

class ElectricCar(Car):
    def show_electric(self):
        print("This is an Electric Car")

e = ElectricCar()

e.show_vehicle()
e.show_car()
e.show_electric()