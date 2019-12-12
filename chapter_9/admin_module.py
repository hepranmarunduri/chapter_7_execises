import user_module
import privileges_module

class Admin(user_module.User):
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
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.faculty = faculty
        self.login_attempts = login_attempts

        admin_privileges = privileges_module.Privileges()
        self.admin_privileges = admin_privileges.privileges