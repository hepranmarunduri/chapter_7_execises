"""
tart with the program you wrote for Exercise 6-1 (page 99).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people . Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

f = {
    'first_initial': 's',
    'last_initial': 'm',
    'birth': 1964,
    'city': 'padang',
    }

lb = {
    'first_initial': 'f',
    'last_initial': 'm',
    'birth': 1996,
    'city': 'jogjakarta',
}

m = {
    'first_initial': 'r',
    'last_initial': 't',
    'birth': 1971,
    'city': None,
}

# Store the dictionaries into a list.
fm = [f, lb, m]

for person in fm:
    print(f"{person}\n")