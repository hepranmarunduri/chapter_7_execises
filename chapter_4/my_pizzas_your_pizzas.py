# See page 65 for detail instruction.

pizzas_from_pizza_hut = ['pepperoni signature', 'splitza signature', 
                    'meat lovers'
                    ]
friend_pizzas = pizzas_from_pizza_hut[:]

pizzas_from_pizza_hut.append('this pizza')
friend_pizzas.append('that pizza')

print("My fav. pizzas:")
for pizza in pizzas_from_pizza_hut:
	print(f"- {pizza}")

print("\nFriend's fav. pizzas:")
for pizza in friend_pizzas:
    print(f"- {pizza}")