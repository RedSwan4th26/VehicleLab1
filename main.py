class Car:
    def __init__(self, make, model, year, weight, num_doors):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors

        print("A Car has been created")

    def display_info(self):
        print(
            f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}\nNumber of Doors: {self.num_doors}")

    def honk(self):
        print("HONK")


class Boat:
    def __init__(self, make, model, year, weight, boat_type):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.boat_type = boat_type

        print("A Boat has been created")

    def display_info(self):
        print(
            f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}\nBoat Type: {self.boat_type}")

    def honk(self):
        print("BEEP")


class Truck:
    def __init__(self, make, model, year, weight, num_doors, payload_capacity):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors
        self.payload_capacity = payload_capacity

        print("A Truck has been created")

    def display_info(self):
        print(
            f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}\nNumber of Doors: {self.num_doors}\nPayload Capacity: {self.payload_capacity}")

    def honk(self):
        print("HONK HONK")

    def dump_load(self):
        print("DUMPING LOAD ....")


aCar = Car("Honda", "Civic", 2020, 2762.0, 4)

aCar.display_info()
aCar.honk()

print("\n")

aBoat = Boat("Yamaha","SX-190",2024,2370.0,"Jet Boat")

aBoat.display_info()
aBoat.honk()

print("\n")

aTruck = Truck("Ford", "Raptor", 2018, 5697.0, 2, 1353.0)

aTruck.display_info()
aTruck.honk()
aTruck.dump_load()