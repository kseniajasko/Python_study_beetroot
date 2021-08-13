# Task 1
#
# Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
# and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person():
    def __init__(self, first_name, last_name, age, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.email = email

    def test1(self):
        return print(self.first_name, self.last_name, self.age, self.phone_number, self.email)

class Student(Person):
    def __init__(self, first_name, last_name, age, phone_number, email, number_class):
        super().__init__(first_name, last_name, age, phone_number, email)
        self.number_class = number_class

class Teacher(Person):
    def __init__(self, first_name, last_name, age, phone_number, email, salary):
        super().__init__(first_name, last_name, age, phone_number, email)
        self.salary = salary

Ok = Student("Ok", "Bor", "15", "056895", "@ghgj", "5")
Mp = Teacher("MP", "Dor", "45", "89524", "@pkn", "1000")
a = Ok.test1()
b = Mp.test1()
