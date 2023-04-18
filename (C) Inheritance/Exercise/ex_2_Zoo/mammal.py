from ex_2_Zoo.animal import Animal


class Mammal(Animal):

    def __init__(self, name: str):
        super().__init__(name)