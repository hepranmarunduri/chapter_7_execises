# See page 43 for detail instruction.

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

print("\nHi everyone, I'm sorry.\nThis morning, "
	"I informed that the table won't arrive in time.\n"
	"It makes me only have table for 2.\nI'm sorry for this.\n")

# Everytime a person is removed, print a message.
pth = guests.pop(0)
print(f"Sorry, {pth}. I will give a bone later..")

tsty = guests.pop(1)
print(f"Sorry, {tsty}. I will give a bone later.")

fsm = guests.pop(2)
print(f"Sorry, {fsm}. I must cancel our dinner.")

ktt = guests.pop(2)
print(f"Sorry, {ktt}. I will give a bone later.\n")

# Send message to remaining guests
print(f"See u at the dinner, {guests[0]}.")
print(f"See u at the dinner, {guests[1]}.\n")

# Empty the list
del guests[0]
del guests[0]
print(guests)