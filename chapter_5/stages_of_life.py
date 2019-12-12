# Write an if-elif-else chain that determines a person’s stage of life.

age = 22

if age < 2:
    person = 'a baby'

elif age < 4:
    person = 'a toddler'

elif age < 13:
    person = 'a kid'

elif age < 20:
    person = 'a teenager'

elif age < 65:
    person = 'an adult'

else:
    person = 'an elder'

print(f"The person is {person}.")