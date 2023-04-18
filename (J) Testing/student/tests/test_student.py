from student.project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("Desi")

    def test_init_without_courses(self):
        self.assertEqual(self.student.name, "Desi")
        self.assertEqual(self.student.courses, {})

    def test_init_with_courses(self):
        self.student.courses = {"Maths": ['excellent']}
        self.assertEqual(self.student.name, 'Desi')
        self.assertEqual(self.student.courses, {"Maths": ['excellent']})

if __name__ == "__main__":
    main()