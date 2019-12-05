"""
Modify your program from Exercise 6-2 so each person can have more than one 
favorite number. Then print each person’s name along with their 
favorite numbers.
"""

favorite_numbers = {
    'h': [22, 1],
    'a': [4, 2],
    'p': [0, 3],
    'm': [1995, 4],
    'hapm': [168, 5],
    }

print(f"Here everyone favorite numbers:")
for name, numbers in favorite_numbers.items():
    print(f"{name.title()} faves:")
    for number in numbers:
        print(f"\t{number}")

    print("")