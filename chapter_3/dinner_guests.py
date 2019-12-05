"""
Working with one of the programs from Exercises 3-4 through 3-7 (page 42), 
use len() to print a message indicating the number of people you are inviting 
to dinner.
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
guests.append('ktt')        #So, I have 6 guests now.

# New invitations
print(f"{invitation_message}{guests[0].title()}?")
print(f"{invitation_message}{guests[1].title()}?")
print(f"{invitation_message}{guests[2].title()}?")
print(f"{invitation_message}{guests[3].title()}?")
print(f"{invitation_message}{guests[4].title()}?")
print(f"{invitation_message}{guests[5].title()}?")


number_of_guests = len(guests)
message = "The number of guests I have invited: "
print(f"{message}{number_of_guests}")