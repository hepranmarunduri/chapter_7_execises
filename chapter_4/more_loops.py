my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('Ini')
friend_foods.append('Itu')

print("My favorite foods are:")
for food in my_foods:
	print(f"- {food.title()}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(f"- {food.title()}")