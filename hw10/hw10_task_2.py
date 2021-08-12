# Task 2
#
# Doggy age
#
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age. Then create a method `human_age` which returns the dog’s age in human equivalent.


class Dog():
    age_factor = 7

    def __init__(self, name, dogs_age):
        self.name = name
        self.dogs_age = dogs_age

    def human_age(self):
        human_equiv = self.dogs_age * self.age_factor
        print(f'The {self.name}’s age in human equivalent: {human_equiv}')

a = Dog('Billy', 3)
a.human_age()


