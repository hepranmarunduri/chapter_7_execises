# See page 112 for detail instruction.

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

fm = [f, lb, m]

for person in fm:
    print(f"{person}\n")