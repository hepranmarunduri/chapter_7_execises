# Ask people the reason of liking programming.

while True:
    ask_reason = input("Why do u like to program?\n(Type 'q' to exit) ")

    if ask_reason == 'q':
        break
    else:
        print("Thanks!\n")
        with open('programming_poll.txt', 'a') as file_object:
            file_object.write(f"{ask_reason}\n")