"""
Think of at least five places in the world you’d like to visit. 
See page 46 for complete instruction.
"""

my_places = ['mecca', 'liverpool', 'tokyo', 'antartic', 'moon']

print(f"{my_places}\n")

# sort the list in alphabetical order temporarily
print(f"{sorted(my_places)}\n")

# original order
print(f"{my_places}\n")

# sort the list in reverse alphabetical order temporarily
print(f"{sorted(my_places, reverse = True)}\n")
print(f"{my_places}\n")

# reverse the order
my_places.reverse()
print(my_places)

# reverse again so the original order backs
my_places.reverse()
print(my_places)

# sort the list elements
my_places.sort()
print(my_places)

# reverse sort the list elements 
my_places.sort(reverse = True)
print(my_places)