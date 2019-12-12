# Polls users about their dream vacation places

# This empty dictionary is for storing user's answers.
user_answers = {}

while True:
    name = input("\nWhat is your name? ")

    question = "If you could visit one place in the world, "
    question += "where would you go? "
    answer = input(question)

    # Store each answer to user_answers dictionary.
    user_answers[name] = answer

    # If the answer is no, the while loop exits.
    next_polling = input("Do you want another person "
                        "to join the polling? (yes/no) ")

    if next_polling == 'no':
        print("Thanks for your participation.")
        break

# This block of code will run if the answer is no.
print("\nThe polling results:")
for name, answer in user_answers.items():
    print(f"- {name.title()} wants to go to {answer.title()}.")