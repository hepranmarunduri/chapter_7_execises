# Ask a user about his/her age and charge him/her based on that age.

prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'q' if you finish.) "

while True:
    message = input(prompt)

    if message == 'q':
        print("THANK U :)")
        break

    age = int(message)
    
    if age < 3:
        price = 0
    elif age < 13:
        price = 10
    else:
        price = 15

    print(f"\nThe cost of your ticket is ${price}.")