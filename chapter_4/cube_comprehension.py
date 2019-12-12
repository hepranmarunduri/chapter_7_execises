# Generate a list of the 10 cubes using a list comprehension.
cubes = [number ** 3 for number in range(1, 11)]
    
for cube in cubes:
    print(cube)