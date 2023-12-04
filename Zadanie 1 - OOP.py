# -*- coding: utf-8 -*-

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

                                                                                                                     
student1 = Student("Basia", [60, 75, 80])
student2 = Student("Adam", [45, 30, 40])

result1 = student1.is_passed()
result2 = student2.is_passed()

print(f"{student1.name} passed: {result1}")
print(f"{student2.name} passed: {result2}")

