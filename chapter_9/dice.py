from random import randint

class Die():
    """Models a dice."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """The dice has 6 die by default."""
        number_of_side = randint(1, self.sides)
        return number_of_side
        

die = Die()

print("6-sided die:")
chance = 1
while chance <= 10:
    chance += 1
    print(die.roll_die())

die.sides = 10
print("\n10-side die:")
chance = 1
while chance <= 10:
    chance += 1
    print(die.roll_die())

die.sides = 20
print("\n20-side die:")
chance = 1
while chance <= 10:
    chance += 1
    print(die.roll_die())