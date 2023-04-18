from Exercise.ex_1_Wild_Cat_Zoo.animal import Animal
from Exercise.ex_1_Wild_Cat_Zoo.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if price > self.__budget:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        try:
            match = [worker for worker in self.workers if worker_name == worker.name][0]
            self.workers.remove(match)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        all_salaries = sum([worker.salary for worker in self.workers])
        if all_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= all_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        needed_money = sum([animal.money_for_care for animal in self.animals])
        if needed_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self) -> str:
        final = [f"You have {len(self.animals)} animals"]
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]
        if lions:
            final.append(f"----- {len(lions)} Lions:")
            for lion in lions:
                final.append(f"{lion.__repr__()}")
        if tigers:
            final.append(f"----- {len(tigers)} Tigers:")
            for tiger in tigers:
                final.append(f"{tiger.__repr__()}")
        if cheetahs:
            final.append(f"----- {len(cheetahs)} Cheetahs:")
            for cheetah in cheetahs:
                final.append(f"{cheetah.__repr__()}")
        return "\n".join(final)

    def workers_status(self) -> str:
        final = [f"You have {len(self.workers)} workers"]
        keepers = [person for person in self.workers if person.__class__.__name__ == "Keeper"]
        caretakers = [person for person in self.workers if person.__class__.__name__ == "Caretaker"]
        vets = [person for person in self.workers if person.__class__.__name__ == "Vet"]
        if keepers:
            final.append(f"----- {len(keepers)} Keepers:")
            for keeper in keepers:
                final.append(f"{keeper.__repr__()}")
        if caretakers:
            final.append(f"----- {len(caretakers)} Caretakers:")
            for caretaker in caretakers:
                final.append(f"{caretaker.__repr__()}")
        if vets:
            final.append(f"----- {len(vets)} Vets:")
            for vet in vets:
                final.append(f"{vet.__repr__()}")
        return "\n".join(final)