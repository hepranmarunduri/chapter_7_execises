# See page 68 for detail instruction.

buffet_foods = ('nasi', 'sayur', 'ayam', 'sambal', 'kerupuk')
print("The menu:")
for food in buffet_foods:
    print(f"- {food.title()}")

print("\nThe menu is updated:")
new_buffet_foods = ('nasi', 'sayur', 'ayam', 'teh', 'ikan')
print("The new menu:")
for food in new_buffet_foods:
    print(f"- {food.title()}")