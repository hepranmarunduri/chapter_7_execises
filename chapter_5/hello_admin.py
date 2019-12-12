# Create a list of several users including an admin for a website..
# Simulate a greeting will appear every time a user logs in.
# But an admin will have a special greeting.

usernames = ['ROCK', 'Duende', 'Python', 'g i n', 'admin']

for username in usernames:
    if username == 'admin':
        print(f"--Hello {username}, would you like to see a status report?--")
    else:
        print(f"Hello {username}, thank you for logging in again.")