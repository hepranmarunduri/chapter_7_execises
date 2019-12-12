from random import choice

def get_winning_ticket(series):
    """Generates a winning ticket. A winning ticket has 4 slots."""
    slot_1 = choice(series)
    slot_2 = choice(series)
    slot_3 = choice(series)
    slot_4 = choice(series)
    winning_ticket = f"{slot_1}{slot_2}{slot_3}{slot_4}"
    
    return winning_ticket

# # Take the first hash to get the wanted result for this program.
# # This happens because this module is imported to lottery_analysis.py.

# # Contains 10 numbers and 5 letters.
# ticket_elements = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'v', 'w', 'x', 'y', 'z')

# print(f"Any ticket matches this ticket, win the prize:")
# print(f"\t\t\t ---- {get_winning_ticket(ticket_elements)} ----")