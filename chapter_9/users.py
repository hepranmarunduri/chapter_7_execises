class User():
    """Models a user with its information."""
    def __init__(self, first_name, last_name, favorite_manga):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_manga = favorite_manga
        self.full_name = f"{first_name} {last_name}"

    def describe_user(self):
        """Displays a summary of user's information."""
        print(f"{self.full_name.title()} likes {self.favorite_manga}.\n")

    def greet_user(self):
        """Greets user."""
        print(f"Hello {self.full_name.title()}.")
        

user_1 = User('masashi', 'kishimoto', 'naruto')
user_2 = User('eiichiro', 'oda', 'one piece')
user_3 = User('tamura', 'yumi', '7 seeds')

user_1.greet_user()
user_1.describe_user()

user_2.greet_user()
user_2.describe_user()

user_3.greet_user()
user_3.describe_user()