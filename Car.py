# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 00:48:39 2019

@author: Aryan Singh
"""

# classes, inheritence with python

class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year=year
        # we can initialize other variables as well
        self.fuel_cap = 15
        self.fuel_level = 0
        
    def fill_tank(self):
        self.fuel_level = self.fill_tank
        print("Fuel tank is filled")
        
    def drive(self):
        print("The car is moving")
        
        
    def add_fuel(self, amount):
        if self.fuel_level+ amount <= self.fuel_capacity:
            self.fuel_level += amount
            print("Added fuel. ")
        else:
            print("The tank can't hold this much")
    
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        
        # Attributes specific to electric cars.
        # Battery capacity in kWh.
        self.battery_size = 70
        self.charge_level = 0

    def charge(self):
        self.charged_level = 100
        print("Fully charged")
    
    
    
my_car = Car('audi','a4',2016) # can make instances like this


print(my_car.make) # audi
print(my_car.model) # a4
print(my_car.year) # 2016

my_ecar = ElectricCar('tesla', 'model s', 2016)
my_ecar.charge()
my_ecar.drive()


'''

Some basic things to remember
$ include the super class name in the parenthesis
$ super().__init__ for the super constructor
 
'''


class Battery():
    def __init__(self, size = 70): # can declare some value as well
        self.size = size
        self.charge_level = 0
        
    def get_range(self):
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270
    
# can also bring in the classes in methods, making an instance of the class
            
'''
from car import Car, ElectricCar
# Make lists to hold a fleet of cars.
    gas_fleet = []
    electric_fleet = []
    
# Make 500 gas cars and 250 electric cars.

for _ in range(500):
    car = Car('ford', 'focus', 2016)
    gas_fleet.append(car)

for _ in range(250):
    ecar = ElectricCar('nissan', 'leaf', 2016)
    electric_fleet.append(ecar)
# Fill the gas cars, and charge electric cars.

for car in gas_fleet:
    car.fill_tank()
for ecar in electric_fleet:
    ecar.charge()

print("Gas cars:", len(gas_fleet))
print("Electric cars:", len(electric_fleet))


'''
        




        