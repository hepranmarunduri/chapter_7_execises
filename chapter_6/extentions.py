# See page 112 for detail instruction.

pizza = {
    'customer': 'rock5396',
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    'size': 'big',
    'number_order': 2,
    }

print(f"There is a new order.")
for pizza_criteria, pizza_criteria_answer in pizza.items():
    order_detail = f"- {pizza_criteria}: {pizza_criteria_answer}"
    
    print(order_detail)