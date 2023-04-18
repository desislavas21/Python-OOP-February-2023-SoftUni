from unittest import TestCase, main


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception("Already fed.")

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception("Cannot sleep while hungry")

        self.sleepy = False

class CatTests(TestCase):

    def test_init(self):
        cat = Cat("Betty")
        self.assertEqual(cat.name, "Betty")
        self.assertEqual(cat.fed, False)
        self.assertEqual(cat.sleepy, False)
        self.assertEqual(cat.size, 0)

    def test_successful_eating_size(self):
        cat = Cat("Betty")
        cat.eat()
        self.assertEqual(cat.size, 1)
        self.assertEqual(cat.fed, True)
        self.assertEqual(cat.sleepy, True)

    def test_successful_sleeping(self):
        cat = Cat("Betty")
        cat.fed = True
        cat.sleepy = True
        cat.sleep()
        self.assertEqual(cat.sleepy, False)

    def test_unsuccessful_eating(self):
        cat = Cat("Betty")
        cat.fed = True

        with self.assertRaises(Exception) as ex:
            cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_unsuccessful_sleep(self):
        cat = Cat("Betty")

        with self.assertRaises(Exception) as ex:
            cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))


if __name__ == '__main__':
    main()