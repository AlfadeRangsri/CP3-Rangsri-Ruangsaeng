class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turnonAirConditioner(self):
        print("Turn on : Air")


class Car(Vehicle):
    color = ""


class Pickup(Vehicle):
    color = ""


class Van(Vehicle):
    color = ""


class EstateCar(Vehicle):
    color = ""


car1 = Car()
car1.color = 'Red'
print("Car's color is :", car1.color)
car1.turnonAirConditioner()

pickUp1 = Pickup()
pickUp1.color = 'Blue'
print("Pickup's color is :", pickUp1.color)
pickUp1.turnonAirConditioner()

van1 = Van()
van1.color = 'Yellow'
print("Van's color is :", van1.color)
van1.turnonAirConditioner()

estateCar1 = EstateCar()
estateCar1.color = 'Gray'
print("EstateCar's color is :", estateCar1.color)
estateCar1.turnonAirConditioner()
