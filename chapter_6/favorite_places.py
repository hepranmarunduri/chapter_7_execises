# See page 112 for detail instruction.

favorite_places = {
                'rock': ['mekah', 'antartic', 'japan'],
                'duende': ['surabaya'],
                'g i n': ['seoul', 'liverpool'],
                }

for name, places in favorite_places.items():
    if name == 'duende':
        print(f"{name.title()}'s favorite place is {places[0].title()}\n")
    else:
        print(f"{name.title()}'s favorite places are:")

        for place in places:
            print(f"\t- {place.title()}")
            
        print("")