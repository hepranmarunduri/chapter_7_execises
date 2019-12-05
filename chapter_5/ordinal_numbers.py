"""
Use an if - elif - else chain inside the loop to print the proper ordinal 
ending for each number.
See page 89 for detail instruction.
"""

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        ordinal_number = f"{number}st"
    elif number == 2:
        ordinal_number = f"{number}nd"
    elif number == 3:
        ordinal_number = f"{number}rd"
    else:
        ordinal_number = f"{number}th"
    
    print(ordinal_number)