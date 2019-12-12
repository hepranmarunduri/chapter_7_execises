# I found bigger table, so I will invite more people.
# Print invitation to each invited person.

guests = ['sm', 'rt', 'fsm']
invitation_message = "would u like to have dinner with me"

print(f"{guests[0]}, {invitation_message}?")
print(f"{guests[1]}, {invitation_message}?")
print(f"{guests[2]}, {invitation_message}?")

print("\nI found a bigger table. So, I will invite more people.\n")

# Add new guest to the beginning of 'guest' list.
guests.insert(0, 'pth')

# Add new guest to the middle of the list.
guests.insert(2, 'tsty')

# Add new guest to the end of the list.
guests.append('ktt')

print(f"{guests[0]}, {invitation_message}?")
print(f"{guests[1]}, {invitation_message}?")
print(f"{guests[2]}, {invitation_message}?")
print(f"{guests[3]}, {invitation_message}?")
print(f"{guests[4]}, {invitation_message}?")
print(f"{guests[5]}, {invitation_message}?")