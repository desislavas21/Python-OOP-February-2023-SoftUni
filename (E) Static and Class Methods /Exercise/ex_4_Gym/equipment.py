import itertools


class Equipment:

    ID = itertools.count(1)

    def __init__(self, name: str):
        self.name = name
        self.id = next(Equipment.ID)

    @staticmethod
    def get_next_id():
        return next(Equipment.ID)

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
