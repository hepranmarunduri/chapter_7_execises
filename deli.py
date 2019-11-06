# Exercise 7-8
# A program to print finished sandwiches.

# The ordered sandwiches.
sandwich_orders = ['tuna', 'cheese', 'extra cheese', 'chicken']
# It is empty because no ordered sandwiches finish.
finished_sandwiches = []

while sandwich_orders:
    # IMPORTANT: Use pop function to move element between the 2 lists.
    sandwich_order = sandwich_orders.pop()

    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

# Show the finished sandwiches.
print("\nAll ordered sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich} sandwich")