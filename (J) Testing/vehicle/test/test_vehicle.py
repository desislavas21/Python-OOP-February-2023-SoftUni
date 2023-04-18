from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(2.50, 100)

    def test_default_fuel_consumption(self):
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 2.50)
        self.assertEqual(self.vehicle.capacity, 2.50)
        self.assertEqual(self.vehicle.horse_power, 100)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_without_enough_fuel(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive(self):
        self.vehicle.fuel = 20
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 20 - 12.5)

    def test_refuel_unsuccessfully(self):
        self.vehicle.fuel = 5
        self.vehicle.capacity = 6

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(4)

        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel(self):
        self.vehicle.fuel = 1
        self.vehicle.capacity = 5
        self.vehicle.refuel(2)
        self.assertEqual(self.vehicle.fuel, 3)

    def test_str(self):
        self.vehicle.fuel = 5
        self.vehicle.fuel_consumption = 2.5
        message = f"The vehicle has 100 " \
                  f"horse power with 5 fuel left and 2.5 fuel consumption"
        self.assertEqual(self.vehicle.__str__(), message)


if __name__ == "__main__":
    main()
