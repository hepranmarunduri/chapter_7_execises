# The objective: Print a message to every person I want to have dinner with.
# See page 42 for detail instruction.

guests = ['sm', 'rt', 'fsm']

invitation_message = "would u like to have dinner with me"
print(f"{guests[0]}, {invitation_message}?")
print(f"{guests[1]}, {invitation_message}?")
print(f"{guests[2]}, {invitation_message}?")

# Show a guest can not come and change the guest.
print(f"\n{guests[1]} can not come to the dinner.\n")
guests[1] = 't'

# New invitations.
print(f"{guests[0]}, {invitation_message}?")
print(f"{guests[1]}, {invitation_message}?")
print(f"{guests[2]}, {invitation_message}?")