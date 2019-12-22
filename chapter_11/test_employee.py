import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Check employee' salary with its bonus."""
    
    def setUp(self):
        self.employee = Employee('jimi', 'hendrix', 100_000)

    def test_give_default_raise(self):
        """
        Check if the default bonus has been added to jimi's salary or not.
        If works well, the salary become $105,000 (salary + bonus)
        """
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 105_000)

    def test_give_custom_raise(self):
        """
        Let's say jimi has got $20,000 as bonus.
        Check if that bonus has been added to jimi's salary or not.
        If works well, the salary become $120,000 (salary + bonus)
        """
        self.employee.give_raise(20_000)
        self.assertEqual(self.employee.salary, 120_000)


if __name__ == '__main__':
    unittest.main()