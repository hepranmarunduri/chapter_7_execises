# See page 105 for detail instruction.

rivers = {
    'batang arau': 'indonesia',
    'han': 'south korea',
    'yellow': 'china',
    }

for river, country in rivers.items():
    print(f"- {river.title()} river is at {country.title()}.")

print("")

for river in rivers:
    print(f"- {river.title()}")

print("")

for country in rivers.values():
    print(f"- {country.title()}")