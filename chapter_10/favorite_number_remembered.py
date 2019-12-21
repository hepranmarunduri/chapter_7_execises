# Combine favorite_number.py and favorite_number_read.py

import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
else:
    print(f"I know your favorite number! It's {favorite_number}.")