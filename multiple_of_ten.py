# Exercise 7-3.
# A program to define a number is a multiple-of-10 number or not.

number = "Tell me a number "
number += "and I tell you it is a multiple-of-10 number or not.\nYour number? "

number = input(number)
number = int(number)

if number % 10 == 0:
    print("\nIt is a multiple-of-10 number.")
else:
    print("\nIt is NOT a multiple-of-10 number.")