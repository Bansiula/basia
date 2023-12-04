# -*- coding: utf-8 -*-

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library\n  City: {self.city}\n  Street: {self.street}\n  Zip Code: {self.zip_code}\n  Open Hours: {self.open_hours}\n  Phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee\n  Name: {self.first_name} {self.last_name}\n  Hire Date: {self.hire_date}\n  Birth Date: {self.birth_date}\n  Address: {self.city}, {self.street}, {self.zip_code}\n  Phone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book\n  Author: {self.author_name} {self.author_surname}\n  Publication Date: {self.publication_date}\n  Number of Pages: {self.number_of_pages}\n  Library: {self.library}"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student\n  Name: {self.name}\n  Marks: {self.marks}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = '\n  '.join(str(book) for book in self.books)
        return f"Order\n  Employee: {self.employee}\n  Student: {self.student}\n  Order Date: {self.order_date}\n  Books:\n  {books_str}"


library1 = Library("Tarnowskie Gory", "Poziomkowa", "42-600", "9-15", "123456789")
library2 = Library("Katowice", "Malinowa", "40-000", "8-18", "987654321")

employee1 = Employee("Barbara", "Babka", "2023-05-12", "1980-08-30", "Katowice", "Pomarańczowa", "40-001", "246897531")
employee2 = Employee("Adam", "Adamski", "2023-08-25", "1970-09-09", "Wrocław", "Truskawkowa", "45-573", "135789642")
employee3 = Employee("Anna", "Agrafka", "2023-12-04", "2000-07-31", "Warszawa", "Złota", "01-125", "123789456")

student1 = Student("Basia", [6, 4, 2])
student2 = Student("Kasia", [5, 3, 4])
student3 = Student("Eliza", [3, 2, 4])

book1 = Book(library1, "2022", "J.R.R.", "Tolkien", 1280)
book2 = Book(library2, "2015", "J.K.", "Rowling", 328)
book3 = Book(library1, "2015", "Charles", "Dickens", 120)
book4 = Book(library2, "374", "Adam", "Mieckiewicz", 350)
book5 = Book(library1, "2017", "Henryk", "Sinekiewicz", 250)

order1 = Order(employee1, student1, [book1, book2], "2023-12-04")
order2 = Order(employee2, student2, [book3, book4, book5], "2023-11-30")


print(order1)
print("\n")
print(order2)