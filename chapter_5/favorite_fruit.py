"""
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
See page 85 for detail instruction.
"""

favorite_fruit = ['kurma', 'banana', 'durian']

if 'kurma' in favorite_fruit:
    print("I like kurma.")
if 'banana' in favorite_fruit:
    print("I like banana.")
if 'durian' in favorite_fruit:
    print("I like durian.")
if 'mango' in favorite_fruit: #Fails because mango is not in the list.
    print("I like mango.")
if 'apple' in favorite_fruit: #Same story with mango.
    print("I like apple.")