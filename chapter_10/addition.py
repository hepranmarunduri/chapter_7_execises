# Handles error: ValueError

try:
    print("\nI can add numbers.\nPlease give me 2 numbers\n")
    
    x = input("First number: ")
    x = int(x)

    y = input("Second number: ")
    y = int(y)

    sum = x + y
except ValueError:
    print("Input numbers only!\n")
else:
    print(f"{sum}\n")