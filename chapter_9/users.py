class User():
    """Models a user profile."""
    def __init__(self, first_name, last_name, department, faculty):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.faculty = faculty
        
    def describe_user(self):
        """Prints a summary of the user. du = describe user"""
        full_name = f"{self.first_name.title()}{self.last_name.title()}"
        
        du = f"{full_name} is a student of {self.department}, {self.faculty}.\n"
        print(du)
        
    def greet_user(self):
        """Prints a personalized greeting to the user."""
        full_name = f"{self.first_name.title()}{self.last_name.title()}"
        print(f"Hi, {full_name}!")
        
        
hm = User('h', 'm', 'economics', 'economy')
fm = User('f', 'm', 'philosophy', 'philosophy')

hm.greet_user()
hm.describe_user()

fm.greet_user()
fm.describe_user()
