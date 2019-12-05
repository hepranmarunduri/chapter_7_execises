"""
Use a dictionary to store people’s favorite numbers. Think of five names, and 
use them as keys in your dictionary. Think of a favorite number for each 
person, and store each as a value in your dictionary. Print each person’s name 
and their favorite number.
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