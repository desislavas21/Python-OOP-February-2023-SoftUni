import itertools


class Customer:

    ID = itertools.count(1)

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = next(Customer.ID)

    @staticmethod
    def get_next_id():
        return next(Customer.ID)

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
