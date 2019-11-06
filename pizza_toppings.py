# Exercise 7-4

prompt = "\nPlease enter your pizza topping:"
prompt += "\n(Enter 'quit' if you finish.) " # q means quit.

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"\n{topping.title()} will added as your pizza topping.")