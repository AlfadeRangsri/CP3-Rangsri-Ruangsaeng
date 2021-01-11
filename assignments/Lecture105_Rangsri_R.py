class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turnonAirConditioner(self):
        print("Turn on : Air")


class Car(Vehicle):
    pass


class Pickup(Vehicle):
    pass


class Van(Vehicle):
    pass


class EstateCar(Vehicle):
    pass


car1 = Car()
car1.turnonAirConditioner()

pickUp1 = Pickup()
pickUp1.turnonAirConditioner()

van1 = Van()
van1.turnonAirConditioner()

estateCar1 = EstateCar()
estateCar1.turnonAirConditioner()
