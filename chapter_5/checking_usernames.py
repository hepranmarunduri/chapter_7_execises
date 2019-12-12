# See page 89 for detail instruction.

current_users = ['Duende', 'g i n', 'ROCK', 'Private Linux', 'Runningman']

new_users = ['Terompet', 'duende', 'gin', 'Rock', 'sandal']

# To make a copy current_users containing the lowercase version of all 
# existing users
# List comprehension version:
#       current_users_lower = [user.lower() for user in current_users]
lower_current_users = []

for current_user in current_users:
    lower_current_users.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"{new_user} is not available! Input another name.")
    else:
        print(f"Welcome, {new_user}!")