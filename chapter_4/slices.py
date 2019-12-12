# See page 65 for detail instruction.

buffet_foods = ('nasi', 'sayur', 'ayam', 'sambal', 'kerupuk')
for food in buffet_foods:
    print(f"- {food.title()}")

print("")

new_buffet_foods = ('nasi', 'sayur', 'ayam', 'teh', 'ikan')
for new_food in new_buffet_foods:
    print(f"- {new_food.title()}")

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