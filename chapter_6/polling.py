# See page 105 for detail instruction.

users = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }

junior_developers = ['thomz', 'jen', 'phil', 'ranchu', 'goele']

for junior_developer in junior_developers:
    if junior_developer in users.keys():
        print(f"Thank you for your participation, {junior_developer.title()}!")
    else:
        print(f"{junior_developer.title()}, would you like to participate in our poll?")
    
    print("")