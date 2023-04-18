import itertools


class Trainer:

    ID = itertools.count(1)

    def __init__(self, name: str):
        self.name = name
        self.id = next(Trainer.ID)

    @staticmethod
    def get_next_id():
        return next(Trainer.ID)

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
