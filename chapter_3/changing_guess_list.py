"""
You just heard that one of your guests can’t make the dinner, so you need to 
send out a new set of invitations. You’ll have to think of someone else to 
invite.
- Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
- Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
- Print a second set of invitation messages, one for each person who is still
in your list.
"""

guests = ['s', 'r', 'f']
invitation_message = "Could you come to my dinner, "

print(f"{invitation_message}{guests[0].title()}?")
print(f"{invitation_message}{guests[1].title()}?")
print(f"{invitation_message}{guests[2].title()}?")

# Show a guest can not come and change the guest.
print(f"\n{guests[1].title()} can not come to the dinner.\n")
guests[1] = 't'

# Print new invitations
print(f"{invitation_message}{guests[0].title()}?")
print(f"{invitation_message}{guests[1].title()}?")
print(f"{invitation_message}{guests[2].title()}?")