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
        

class Admin(User):
    """Models a special user: admin."""
    def __init__(self, first_name, last_name, favorite_manga, login_attempts,
                privileges):

        super().__init__(first_name, last_name, favorite_manga, login_attempts)
    
        self.privileges = privileges

    def show_privileges(self):
        """Display all privileges."""
        print("Admin's privileges:")

        for privilege in self.privileges:
            print(f"- {privilege}")
            

admin_privileges = ['can add post', 'can delete post', 'can ban user']

admin = Admin('the', 'admin', 'lookism', None, admin_privileges)

admin.show_privileges()