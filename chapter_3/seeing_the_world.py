# See page 46 for detail instruction.

desirable_places = ['mecca', 'liverpool', 'tokyo', 'antartic', 'moon']

print(f"{desirable_places}\n")

# Sort the list in alphabetical order temporarily
print(f"{sorted(desirable_places)}\n")

# Original order
print(f"{desirable_places}\n")

# Sort the list in reverse alphabetical order temporarily
print(f"{sorted(desirable_places, reverse = True)}\n")
print(f"{desirable_places}\n")

# Reverse the order
desirable_places.reverse()
print(desirable_places)

# Reverse again so the original order backs
desirable_places.reverse()
print(desirable_places)

# Sort the elements the list.
desirable_places.sort()
print(desirable_places)

# Reverse sort the list elements 
desirable_places.sort(reverse = True)
print(desirable_places)