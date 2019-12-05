"""
A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
- Use a for loop to print each food the restaurant offers.
- Try to modify one of the items, and make sure that Python rejects the
change.
- The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
"""

buffet_foods = ('nasi', 'sayur', 'ayam', 'sambal', 'kerupuk')
for food in buffet_foods:
    print(f"- {food.title()}")

new_buffet_foods = ('nasi', 'sayur', 'ayam', 'teh', 'ikan')
print("")
for new_food in new_buffet_foods:
    print(f"- {new_food.title()}")