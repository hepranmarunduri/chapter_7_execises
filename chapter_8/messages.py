def show_messages(messages):
    """Print each messages in a list."""
    for message in messages:
        print(f"- {message.title()}.")


lang_messages = ['python', 'java', 'c++', 'kotlin', 'c', 'go', 'php']

show_messages(lang_messages)