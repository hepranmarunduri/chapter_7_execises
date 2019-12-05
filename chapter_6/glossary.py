# See page 99 for instruction.

glossary = {
    'loop': 'accesses all element in a list',
    'dictionary': 'has at least one key-value pair in it',
    'comment': 'a guidance or a note for code',
    'text_editor': 'a place where to type source code',
    'print()': 'a function to print message or value',
    }

for term, meaning in glossary.items():
    print(f"{term.title()}: {meaning}.\n")