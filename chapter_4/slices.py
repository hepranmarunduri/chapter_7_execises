"""
Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
- Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
- Print the message Three items from the middle of the list are:. Use a slice to
print three items from the middle of the list.
- Print the message The last three items in the list are:. Use a slice to print the
last three items in the list.
"""

buffet_foods = ('nasi', 'sayur', 'ayam', 'sambal', 'kerupuk')
for food in buffet_foods:
    print(food.title())

new_buffet_foods = ('nasi', 'sayur', 'ayam', 'teh', 'ikan')
print("")
for new_food in new_buffet_foods:
    print(new_food.title())

print("\nThe first three items in the list are:")
first_3 = buffet_foods[0:3]
for food in first_3:
    print(f"- {food.title()}")

print("\nThree items from the middle of the list are:")
middle_3 = buffet_foods[1:4]
for food in middle_3:
    print(f"- {food.title()}")

print("\nThe last three items in the list are:")
last_3 = buffet_foods[-3:]
for food in last_3:
    print(f"- {food.title()}")