# Check for certain element in a list using if statement.

favorite_fruit = ['kurma', 'banana', 'durian']

if 'kurma' in favorite_fruit:
    print("I like kurma.")

if 'banana' in favorite_fruit:
    print("I like banana.")

if 'durian' in favorite_fruit:
    print("I like durian.")

#Fails because mango is not in the list.
if 'mango' in favorite_fruit: 
    print("I like mango.")

#Same story with mango.
if 'apple' in favorite_fruit: 
    print("I like apple.")