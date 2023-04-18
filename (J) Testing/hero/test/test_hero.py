from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("username", 1, 10, 2)

    def test_init(self):
        self.assertEqual(self.hero.username, "username")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 10)
        self.assertEqual(self.hero.damage, 2)

    def test_battle_with_yourself(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero("username", 2, 4, 5))

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_without_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(Hero("kity", 2, 4, 5))
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_low_health(self):
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(Hero("kity", 2, -3, 5))
        self.assertEqual(str(ex.exception), "You cannot fight kity. He needs to rest")

    def test_battle_draw(self):
        self.hero.health = 1
        message = self.hero.battle(Hero("kity", 2, 1, 5))
        self.assertEqual(message, "Draw")

    def test_battle_win(self):
        self.hero.health = 100
        message = self.hero.battle(Hero("kity", 2, 1, 5))
        self.assertEqual(message, "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.damage, 7)
        self.assertEqual(self.hero.health, 95)

    def test_battle_loss(self):
        self.hero.health = 3
        enemy = Hero('kity', 2, 100, 5)
        message = self.hero.battle(enemy)
        self.assertEqual(message, "You lose")
        self.assertEqual(enemy.level, 3)
        self.assertEqual(enemy.health, 103)
        self.assertEqual(enemy.damage, 10)

    def test_str(self):
        message = f"Hero username: 1 lvl\n" \
               f"Health: 10\n" \
               f"Damage: 2\n"
        self.assertEqual(message, self.hero.__str__())


if __name__ == "__main__":
    main()