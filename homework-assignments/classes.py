# Assignment: Classes
# Class: pirple.com course "Python is Easy"
# Written by Franz A. Tapia Chaca
# Last updated on 09 April 2021

# Two types of vehicles are created.
# They take trips and depending on the number of trips, they require maintenance before further travelling


class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight  # in kg
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0

    # Function: Repair after a certain amount of travelling
    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False


class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False # i.e. is in current motion

    # Begin driving
    def drive(self):
        self.isDriving = True

    # Stop driving
    def stop(self):
        self.isDriving = False
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True

    def __str__(self):
        return "Car with make " + self.make + ", model " + self.model + ", year " + self.year + " and weight " + \
               str(self.weight) + " kg: Trips since maintenance: " + str(self.tripsSinceMaintenance) +  \
               ". Needs maintenance? " + str(self.needsMaintenance)


class Planes(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = False

    # Begin flying
    def fly(self):
        if self.needsMaintenance:
            print("The plane cannot fly until it's repaired.")
            return False  # plane did not take off
        else:
            self.isFlying = True
            return True  # plane took off

    # Land
    def land(self):
        self.isFlying = False
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True

    def __str__(self):
        return "Plane with make " + self.make + ", model " + self.model + ", year " + self.year + " and weight " + \
               str(self.weight) + " kg: Trips since maintenance: " + str(self.tripsSinceMaintenance) +  \
               ". Needs maintenance? " + str(self.needsMaintenance)


# Define three car objects
Car1 = Cars("Bugatti", "Divo", "2018", 1960)
Car2 = Cars("Lamborghini", "Sian FKP 37", "2020", 2000)
Car3 = Cars("Volkswagen", "Beetle", "1997", 840)

# Drive the cars
# Car 1
for trip in range(50):
    Car1.drive()
    Car1.stop()
print(Car1)
if Car1.needsMaintenance:
    Car1.repair()
    print(Car1)

# Car 2
for trip in range(100):
    Car2.drive()
    Car2.stop()
print(Car2)
if Car2.needsMaintenance:
    Car2.repair()
    print(Car2)

# Car 3
for trip in range(101):
    Car3.drive()
    Car3.stop()
print(Car3)
if Car3.needsMaintenance:
    Car3.repair()
    print(Car3)

input("Press Enter to continue. ")

# Flying the plane
Plane1 = Planes("Boeing", "747", "1968", 183500)
while True:
    print(Plane1)
    tookOff = Plane1.fly()
    if tookOff:
        Plane1.land()
    else:
        desireToRepair = input("Do you wish to repair the plane? (Y/N) ")
        if desireToRepair == ("y" or "Y"):  # parentheses needed to correctly evaluate if statement
            Plane1.repair()
        else:
            continue
