# Ask a user how many people are in his/her dinner group.
# If the people < 8, the table is ready.
# Otherwise, no.

message = input("How many people are in your dinner group? ")
people = int(message)

if people > 8:
    print("\nSorry, you'll have to wait for a table.")
else:
    print("\nA table is available fo you!")