from ex_4_Multilevel_Inheritance.person import Person
from ex_4_Multilevel_Inheritance.employee import Employee


class Teacher(Person, Employee):

    def teach(self):
        return "teaching..."
