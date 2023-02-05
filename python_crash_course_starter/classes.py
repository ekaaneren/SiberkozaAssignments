# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
class Vehicle:
    def __init__(self, license_no, age):
        self.license_no = license_no
        self.age = age
        self._has_insurrance = True

    def has_birthday(self):
        self.age += 1

    def print_encap(self):
        print(self._has_insurrance)


class Car(Vehicle):
    def __init__(self, license_no, age, has_fine, fine_amount):
        super().__init__(license_no, age)
        self.has_fine = has_fine
        self.fine_amount = fine_amount

    def fine(self, amount):
        self.has_fine = True
        self.fine_amount = amount

    def forgive(self):
        self.has_fine = False
        self.fine_amount = 0

    def get_fine(self):
        return self.fine_amount

plane_ke = Vehicle(1022,22)
plane_ke.print_encap()
plane_ke.has_birthday()
print(plane_ke.age)

car_ke = Car(9346,11,False,0)
print(car_ke.get_fine())
car_ke.fine(100)
print(car_ke.get_fine())
