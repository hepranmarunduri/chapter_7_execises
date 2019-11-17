# Exercise 7-2.
# A program to tell user for seat availability.

seat = input("How many seat do you need? ")
seat = int(seat)

if seat <= 8:
    print("\nThe table is available for you.")
else:
    print("\nSorry, you will need to wait.")
