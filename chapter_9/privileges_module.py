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