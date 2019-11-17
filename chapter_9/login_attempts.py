# Start from users.py
# Add an attribute login_attempts.
class User:
    """Model a user"""
    def __init__(
        self, first_name, last_name,
        favorite_manga, favorite_anime,
        login_attempts
        ):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_manga = favorite_manga
        self.favorite_anime = favorite_anime
        self.login_attempts = login_attempts

    def describe_user(self):
        describer = f"You, {self.first_name.title()} {self.last_name.title()},"
        describer += f" likes {self.favorite_manga.title()} (manga) "
        describer += f"and {self.favorite_anime.title()} (anime).\n"

        print(describer)

    def greet_user(self):
        print(f"Hi {self.first_name.title()} {self.last_name.title()}!")

    # Increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts
        
    # Resets the value of login_attempts to 0.
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

# An instance of 'user'.
user = User('komi', 'san', 'komi-san', 'tonari no totoro', 0)

# Call the method that increment user's login attempts.
while user.login_attempts < 8:
    user.increment_login_attempts()

# Checking the increment works.
print("Total login attempts:")
print(f"{user.login_attempts}")

# Checking the reset works.
print("\nReset user's login attempts:")
user.reset_login_attempts()
print(f"{user.login_attempts}")