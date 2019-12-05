"""
Make a dictionary called favorite_places . Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
"""

favorite_places = {
    'rock': ['mekah', 'antartic', 'japan'],
    'duende': ['surabaya'],
    'g i n': ['seoul', 'liverpool'],
    }

# Show the information in the dictionary
for name, places in favorite_places.items():
    if name == 'duende':
        print(f"{name.title()}'s favorite place is {places[0].title()}\n")

    else:
        print(f"{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t- {place.title()}")
        print("")