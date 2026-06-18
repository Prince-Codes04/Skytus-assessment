class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount):
        self.price = self.price - (self.price * discount / 100)

    def display(self):
        print("\nLaptop Details")
        print("Brand :", self.brand)
        print("Final Price :", self.price)

brand = input("Enter Laptop Brand: ")
price = float(input("Enter Laptop Price: "))
discount = float(input("Enter Discount Percentage: "))

laptop = Laptop(brand, price)

laptop.apply_discount(discount)
laptop.display()