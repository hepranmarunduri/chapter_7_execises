# Ask user a number and tell whether it's a multiple of 10 number or not.

prompt = "Tell me a number, and I'll tell you"
prompt += " whether the number is a multiple of 10 or not.\nYour number? "

answer = input(prompt)

number = int(answer)

if number % 10 == 0:
    print(f"\nYour number, {number}, is a multiple of 10.")

else:
    print(f"\nYour number, {number}, is NOT a multiple of 10.")