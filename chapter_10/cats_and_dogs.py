# Handles error.

filenames = ['cats.txt', 'dogs.txt']

try:
    for filename in filenames:
        with open(filename) as file:
            print(f"- {filename}")
            print(f"{file.read()}\n")
except FileNotFoundError:
    print(f"{filename} is missing!")