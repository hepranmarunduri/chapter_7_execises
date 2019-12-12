from random import choice
from lottery import get_winning_ticket as gwt

def get_ticket(series):
    """Generates a ticket."""
    slot_1 = choice(series)
    slot_2 = choice(series)
    slot_3 = choice(series)
    slot_4 = choice(series)

    ticket = f"{slot_1}{slot_2}{slot_3}{slot_4}"
    return ticket

def check_ticket(ticket, winning_ticket):
    """
    Always checks ticket to winning ticket until they match.
    Because it should returns True, the if statement will always run.
    """
    if ticket != winning_ticket:
        return False

    return True


ticket_elements = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'v', 'w', 'x', 'y', 'z')

winning_ticket = gwt(ticket_elements)

plays = 0
won = False

# This is for the available chances.
max_chances = 1_000_000

while not won:
    # Everytime ticket does not match the winning ticket.
    # A new ticket and a new winning ticket are picked.
    ticket = get_ticket(ticket_elements)
    won = check_ticket(ticket, winning_ticket)

    plays += 1
    if plays >= max_chances:
        break

# The if statement will run when the result is True.
# Since the result mostly will False, it will repeat and repeat until the 
# plays reaches 1_000_000 (max_chances value).
if won:
    print("------ You win. ------")
    print(f"Your ticket: {ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"You tried {plays} times.")
    
else:
    print(f"You tried {plays} times, without win.")
    print(f"Your ticket: {ticket}")
    print(f"Winning ticket: {winning_ticket}")