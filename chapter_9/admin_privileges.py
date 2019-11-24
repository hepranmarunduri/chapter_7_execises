from user import User

class Privileges():
    """Models a list of privileges"""
    def __init__(self):
        self.privileges = ('can add post', 'can delete post', 'can ban user')
        
    def show_privileges(self):
        """Shows all privileges."""
        print(f"Hi. These are your privileges:")
        privileges = self.privileges
        for privilege in privileges:
            print(f"- You {privilege}.")

class Admin(User):
    """Models an admin who is a special type of user."""
    def __init__(
            self, first_name, last_name,
            department, faculty, login_attempts
            ):
        """Admin has privileges that separates from other user."""
        super().__init__(
                    first_name, last_name, department,
                    faculty, login_attempts
                    )
        self.department = department
        self.faculty = faculty
        self.login_attempts = login_attempts
        self.admin_privileges = Privileges()

