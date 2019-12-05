"""
Make several dictionaries, where each dictionary represents a differ-
ent pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets . Next, loop through your list and as
you do, print everything you know about each pet.
"""
tasty = {
    'kind': 'cat',
    'owner': 'me and lb',
    }

putih_owner = ('m', 'me', 'lb')
putih = {
    'kind': 'cat',
    'owner': putih_owner,
    }

# Store each dictionaries into this list.
pets = [tasty, putih]

# Show each pet information (using loop)
for pet in pets:
    print(f"{pet}\n")