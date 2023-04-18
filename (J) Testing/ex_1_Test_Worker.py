from unittest import TestCase, main


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} have saved {self.money} money."


class WorkerTests(TestCase):

    def test_init(self):
        t = Worker("George", 1000, 1200)
        self.assertEqual(t.name, "George")
        self.assertEqual(t.salary, 1000)
        self.assertEqual(t.energy, 1200)
        self.assertEqual(t.money, 0)

    def test_rest(self):
        t = Worker("George", 1000, 1200)
        t.rest()
        self.assertEqual(t.energy, 1201)

    def test_not_able_to_work(self):
        t = Worker("George", 1000, 0)

        with self.assertRaises(Exception) as ex:
            t.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work(self):
        t = Worker("George", 1000, 1200)
        t.work()
        self.assertEqual(t.money, 1000)
        self.assertEqual(t.energy, 1199)

    def test_get_info(self):
        t = Worker("George", 1000, 1200)
        self.assertEqual("George have saved 0 money.", t.get_info())


if __name__ == '__main__':
    main()
