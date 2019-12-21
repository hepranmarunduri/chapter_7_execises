# Handles error: ValueError in a loop.

while True:
    try:
        print("\nI can add numbers. Please give me 2 numbers.\n"
            "(Enter 'q' to quit.)\n")
        
        x = input("First number: ")
        if x == 'q':
            break
        x = int(x)


        y = input("Second number: ")
        if y == 'q':
            break
        y = int(y)

        sum = x + y
    except ValueError:
        print("Input numbers only!")
    else:
        print(f"{sum}")
