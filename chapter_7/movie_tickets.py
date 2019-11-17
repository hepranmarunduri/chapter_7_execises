# Exercise 7-5
# A program to charge customer based on its age.

prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'q' if you finish.) "

while True:
    message = input(prompt)
    if message == 'q':
        print("THANK U :)")
        break

    age = int(message)
    
    if age < 3:         # It's free if under 3.
        price = 0
    elif age < 13:      # Between 3 - 12, it's $10.
        price = 10
    else:               # More than 12 years old, it's $15.
        price = 15

    print(f"\nThe cost of your ticket is ${price}.")
