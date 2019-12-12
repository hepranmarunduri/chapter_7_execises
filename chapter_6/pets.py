# See page 112 for detail instruction.

tasty = {
    'kind': 'cat',
    'owner': 'me and lb',
    }

putih_owner = ('m', 'me', 'lb')
putih = {
    'kind': 'cat',
    'owner': putih_owner,
    }

pets = [tasty, putih]

for pet in pets:
    print(f"{pet}\n")