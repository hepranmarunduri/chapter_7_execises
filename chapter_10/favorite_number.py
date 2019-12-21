# Store a user's favorite number by json.dump()

import json

favorite_number = input("What is your favorite number? ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)