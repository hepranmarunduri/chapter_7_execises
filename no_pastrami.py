# Exercise 7-9
# A program to tell that the pastrami sandwich is running out of stock.

# There are 3 orders of pastrami.
sandwich_orders = ['tuna', 'pastrami', 'cheese', 'pastrami', 'pastrami', 'extra cheese', 'chicken']
# It is empty because no ordered sandwiches finish.
finished_sandwiches = []

# Remove all orders to pastrami and informs the user.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("Sorry, we are running out of pastrami.\n")

while sandwich_orders:
    # IMPORTANT: Use pop function to move element between the 2 lists.
    sandwich_order = sandwich_orders.pop()

    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

# Show the finished sandwiches.
print("\nAll ordered sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich} sandwich")