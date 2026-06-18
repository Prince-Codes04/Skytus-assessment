class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat Booked Successfully")
        else:
            print("No Seats Available")

    def display(self):
        print("Available Seats :", self.seats)

seats = int(input("Enter Total Seats: "))

flight = Flight(seats)

flight.book_seat()
flight.display()