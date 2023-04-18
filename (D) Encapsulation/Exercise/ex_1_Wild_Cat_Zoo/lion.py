from Exercise.ex_1_Wild_Cat_Zoo.animal import Animal

class Lion(Animal):

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=50)

