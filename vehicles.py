class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Vroom vroom! Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Whoosh! Flying ✈️")


transport = [Car(), Plane()]
for t in transport:
    t.move()
