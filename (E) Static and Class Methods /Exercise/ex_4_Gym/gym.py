from Exercise.ex_4_Gym.customer import Customer
from Exercise.ex_4_Gym.trainer import Trainer
from Exercise.ex_4_Gym.equipment import Equipment
from Exercise.ex_4_Gym.subscription import Subscription
from Exercise.ex_4_Gym.exercise_plan import ExercisePlan
from typing import List


class Gym:

    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [subscription for subscription in self.subscriptions if subscription_id == subscription.id][0]
        customer = [customer for customer in self.customers if subscription.customer_id == customer.id][0]
        trainer = [trainer for trainer in self.trainers if subscription.trainer_id == trainer.id][0]
        plan = [plan for plan in self.plans if plan.trainer_id == trainer.id][0]
        equipment = [equipment for equipment in self.equipment if plan.equipment_id == equipment.id][0]
        return "\n".join([subscription.__repr__(), customer.__repr__(), trainer.__repr__(), equipment.__repr__(),
                          plan.__repr__()])

