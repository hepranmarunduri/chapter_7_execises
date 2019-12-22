class Employee():
    """Model an employee with its annual salary."""

    def __init__(self, first, last, salary):
        """first = first name, last = last name & salary = annual salary"""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, bonus=5000):
        """The default bonus is $5,000 but it can vary depends on situation."""
        self.salary = self.salary + bonus