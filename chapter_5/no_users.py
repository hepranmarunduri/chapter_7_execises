# Add an if test to hello_admin.py to make sure the list of 
# users is not empty. See page 89 for detail instruction.

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"--Hello {username}, "
                "would you like to see a status report?""--"
                )
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")