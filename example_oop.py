# Car design
class Car:
    def __init__(self, fuel, brand):
        self.wheel = 4
        self.fuel = fuel
        self.brand = brand

    def run(self, maxspeed):
        print(f"Car {self.brand} with current maxspeed {maxspeed} km/h")

    def light(self, light_length):
        print(f"Car {self.brand} light far {light_length} m")

# Car details
car1 = Car("Electric", "Vinfast")
print(car1.wheel)
print(car1.fuel)
print(car1.brand)

car1.run(60)
               