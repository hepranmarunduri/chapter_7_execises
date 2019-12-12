def send_messages(messages, sent_messages):
    """
    Print each messages in a list.
    Then, as a message printed, move each messages to a new list.
    """
    while messages:
        for message in messages:
            print(f"- {message.title()}.")
            print("Sending message...\n")
            send_message = messages.pop()

            sent_messages.append(send_message)


messages = ['python', 'java', 'c++', 'kotlin', 'c', 'go', 'php']

sent_messages = []

print("Before:")
print(messages)
print(f"{sent_messages}\n")

# Pass a copy of list 'messages' as the argument.
send_messages(messages[:], sent_messages)

print("After:")
print(f"{messages}")
print(sent_messages)