import unittest
from my_module import max3, odd, majority, Employee, Manager


class TestModule(unittest.TestCase):
    def test_max3(self):        
        self.assertEqual(max3(5, 3, 1.8), 5)
        self.assertEqual(max3(2.5, 3.7, 1.8), 3.7)
        self.assertEqual(max3(7, 5.5, 6), 7)

    def test_odd(self):
        self.assertEqual(odd(True, False, True), False)
        self.assertEqual(odd(True, True, True), True)
        self.assertEqual(odd(False, False, False), False)
        
    def test_majority(self):
        self.assertEqual(majority(True, True, False), True)
        self.assertEqual(majority(False, True, False), False)
        self.assertEqual(majority(False, False, False), False)

class TestEmpModule(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee("Bob", 7)

    def test_name(self):
        self.assertEqual(self.employee1.name, "Bob")

    def test_salary(self):
        self.assertEqual(self.employee1.salary, 7)

class TestManModule(unittest.TestCase):
    
    def setUp(self):
        self.manager1 = Manager("Steve", 14, "Management")

    def test_name(self):
        self.assertEqual(self.manager1.name, "Steve")

    def test_salary(self):
        self.assertEqual(self.manager1.salary, 14)
        
    def test_dept(self):
        self.assertEqual(self.manager1.dept, "Management")
    
    def test_get_details(self):
        self.assertEqual(self.manager1.get_details(), "Name: Steve, Salary: 14, Department: Management")
    
if __name__ == '__main__':
    unittest.main()
    