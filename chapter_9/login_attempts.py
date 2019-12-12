class User():
    """Models a user with its information."""
    def __init__(self, first_name, last_name, favorite_manga, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_manga = favorite_manga
        self.full_name = f"{first_name} {last_name}"
        self.login_attempts = login_attempts

    def describe_user(self):
        """Displays a summary of user's information."""
        print(f"{self.full_name.title()} likes {self.favorite_manga}.\n")

    def greet_user(self):
        """Greets user."""
        print(f"Hello {self.full_name.title()}.")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        """Resets the value of login attempts to 0."""
        self.login_attempts = 0
        return self.login_attempts
        

user = User('masashi', 'kishimoto', 'naruto', 0)

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Shows the total login attempts.
print(f"Total login: {user.login_attempts}")

user.reset_login_attempts()

# Resets a user's total login attempts.
print(f"Total login: {user.login_attempts}")