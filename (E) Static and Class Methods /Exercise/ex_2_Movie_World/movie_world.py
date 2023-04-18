from typing import List
from Exercise.ex_2_Movie_World.customer import Customer
from Exercise.ex_2_Movie_World.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):

        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):

        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):

        try:
            customer = [customer for customer in self.customers if customer.id == customer_id][0]
            dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"

            if dvd.is_rented:
                return "DVD is already rented"

            if customer.age < dvd.age_restriction:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

            dvd.is_rented = True
            customer.rented_dvds.append(dvd)
            return f"{customer.name} has successfully rented {dvd.name}"

        except IndexError:
            pass

    def return_dvd(self, customer_id: int, dvd_id: int):

        try:
            customer = [customer for customer in self.customers if customer.id == customer_id][0]
            dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

            if dvd not in customer.rented_dvds:
                return f"{customer.name} does not have that DVD"

            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        except IndexError:
            pass

    def __repr__(self):
        final = []
        for customer in self.customers:
            final.append(customer.__repr__())
        for dvd in self.dvds:
            final.append(dvd.__repr__())
        return '\n'.join(final)

