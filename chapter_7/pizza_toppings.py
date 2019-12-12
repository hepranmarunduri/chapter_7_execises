# Always ask a user to enter a series of pizza toppings
# until he/she enter a 'quit' value.
prompt = "\nPlease enter your pizza topping:"
prompt += "\n(Enter 'quit' if you finish.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"\n{topping.title()} will added as your pizza topping.")