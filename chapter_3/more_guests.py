"""
You just found a bigger dinner table, so now more space is available. Think of 
three more guests to invite to dinner.
- Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
- Use insert() to add one new guest to the beginning of your list.
- Use insert() to add one new guest to the middle of your list.
- Use append() to add one new guest to the end of your list.
- Print a new set of invitation messages, one for each person in your list.
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

print("\nHi everyone, I just found a bigger table. "
    "So, I let another to join.\n")

# New guest at the beginning of the list
guests.insert(0, 'p')
# New guest at the middle
guests.insert(2, 'pth')
# New guest at the end
guests.append('ktt')		#So, I have 6 guests now.

# New invitations
print(f"{invitation_message}{guests[0].title()}?")
print(f"{invitation_message}{guests[1].title()}?")
print(f"{invitation_message}{guests[2].title()}?")
print(f"{invitation_message}{guests[3].title()}?")
print(f"{invitation_message}{guests[4].title()}?")
print(f"{invitation_message}{guests[5].title()}?")