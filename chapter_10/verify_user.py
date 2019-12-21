import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except Exception:
        return None
    else:
        return username

def get_new_username():
    """Prompt a new username."""
    username = input("What is your name? " )
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        while True:
            question = input(f"Are you {username}? (y/n) ")
            if question == 'y':
                print(f"Welcome back, {username}!\n")
                break
            elif question == 'n':
                print("\nSo, this is your first time here.")
                get_new_username()
                print(f"Ok.\n")
                break
            else:
                print("Wrong input. Try again.\n")
                continue
    else:
        username = get_new_username()
        print(f"We'll remember u when u come back, {username}!\n")


greet_user()