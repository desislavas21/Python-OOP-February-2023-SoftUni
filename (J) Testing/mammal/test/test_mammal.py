from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("goti", "monkey", "krq")

    def test_init(self):
        self.assertEqual("goti", self.mammal.name)
        self.assertEqual("monkey", self.mammal.type)
        self.assertEqual("krq", self.mammal.sound)

    def test_make_sound(self):
        self.assertEqual(f"goti makes krq", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"goti is of type monkey", self.mammal.info())


if __name__ == "__main__":
    main()
