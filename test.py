import unittest
from my_module import max3, odd, majority, Employee


class TestModule(unittest.TestCase):
    def test_max3(self):
        result = max3(5, 3, 1.8)
        
        self.assertEqual(result, 5)

    def test_odd(self):
        result = odd(True, False, True)

        self.assertEqual(result, False)

    def test_majority(self):
        result = majority(True, True, False)

        self.assertEqual(result, True)

class TesparentModule(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee("Bob", "$7")

    def test_name(self):
        self.assertEqual(self.employee1.name, "Bob")

    def test_salary(self):
        self.assertEqual(self.employee1.salary, "$7")

if __name__ == '__main__':
    unittest.main()
    