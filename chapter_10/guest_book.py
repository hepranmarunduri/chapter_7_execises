# Prompts users for their name. Then write the name in a text file.
condition = True

while condition:
    ask_name = input("Who are you?\n(Enter 'q' to quit.) ")

    if ask_name == 'q':
        condition = False
    else:
        with open('guest_book.txt', 'a') as file_object:
            # Because of /n, each name has its own line.
            file_object.write(f"{ask_name}\n")
        print(f"Hi {ask_name.title()}!\n")