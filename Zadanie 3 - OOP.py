# -*- coding: utf-8 -*-

class Property:
   def __init__(self, area, rooms, price, address):
       self.area = area
       self.rooms = rooms
       self.price = price
       self.address = address

   def __str__(self):
       return f"Property: {self.area} sqm, {self.rooms} rooms, priced at {self.price}, located at {self.address}"

class House(Property):
   def __init__(self, area, rooms, price, address, plot):
       super().__init__(area, rooms, price, address)
       self.plot = plot

   def __str__(self):
       return f"House: {self.area} sqm, {self.rooms} rooms, priced at {self.price}, located at {self.address}, plot size {self.plot} sqm"

class Flat(Property):
   def __init__(self, area, rooms, price, address, floor):
       super().__init__(area, rooms, price, address)
       self.floor = floor

   def __str__(self):
       return f"Flat: {self.area} sqm, {self.rooms} rooms, priced at {self.price}, located at {self.address}, on floor {self.floor}"


house = House(area=240, rooms=5, price=1500000, address="Poziomkowa", plot=500)


flat = Flat(area=80, rooms=3, price=400000, address="Malinowa", floor=3)


print(house)
print(flat)
