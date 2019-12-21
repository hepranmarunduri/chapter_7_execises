# Prompts a user's name then store that name to a text file.

ask_name = input("Who are you? ")

with open('guest.txt', 'w') as file_object:
    file_object.write(f"{ask_name}\n")