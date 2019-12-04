"""
You just found out that your new dinner table won’t arrive in time for the 
dinner, and you have space for only two guests.
- Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
- Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
- Print a message to each of the two people still on your list, letting them
know they’re still invited.
- Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
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

# Apologize message.
print("\nHi everyone, I'm sorry. This morning, "
	"I informed that the table won't arrive in time. "
	"It makes me only have table for 2. I'm sorry for this.\n")

print(guests)

p = guests.pop(0)
print(f"Sorry, {p.title()}. I must cancel our dinner.")

pth = guests.pop(1)
print(f"Sorry, {pth.title()}. I must cancel our dinner.")

t = guests.pop(1)
print(f"Sorry, {t.title()}. I will give a bone later.")

f = guests.pop(2)
print(f"Sorry, {f.title()}. I will give a bone later.\n")

# Send message to remaining guests
print(f"See u at table, {guests[0].title()}.")
print(f"See u at table, {guests[1].title()}.\n")

# Empty the list
del guests[0]
del guests[0]
print(guests)