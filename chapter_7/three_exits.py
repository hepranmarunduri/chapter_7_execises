# # The conditional test will stop the while loop.
# prompt = "\nPlease enter your age:"
# prompt += "\n(Enter 'q' if you finish.) "

# message = ""
# while message != 'q':
#     message = input(prompt)
#     if message != 'q':
#         age = int(message)

#         if age != 'q':
#             if  age < 3:
#                 price = 0
#             elif age <= 12:
#                 price = 10
#             elif age > 12:
#                 price = 15
            
#         print(f"\nThe cost of your ticket is ${price}.")

# # A flag to control how long the loop runs.
# prompt = "\nPlease enter your age:"
# prompt += "\n(Enter 'q' if you finish.) "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'q':
#         active = False
        
#     else:
#         age = int(message)
#         if  age < 3:
#             price = 0
#         elif age <= 12:
#             price = 10
#         elif age > 12:
#             price = 15
#         print(f"\nThe cost of your ticket is ${price}.")

# A break statement to exit the loop when the user enters a 'quit' value.
prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit' if you finish.) "

while True:
    message = input(prompt)

    if message == 'quit':
        break

    age = int(message)

    if  age < 3:
        price = 0
    elif age <= 12:
        price = 10
    elif age > 12:
        price = 15
    print(f"\nThe cost of your ticket is ${price}.")
