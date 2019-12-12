# See page 105 for detail instruction.

glossary = {
        'loop': 'accesses all element in a list',
        'dictionary': 'has at least one key-value pair in it',
        'comment': 'a guidance or a note for code',
        'text_editor': 'a place where to type source code',
        'print()': 'a function to print message or value',
        'key-value': 'the contain of dictionary',
        'set': 'a function to eliminate similar element',
        'sorted': 'a function to arrange element into alphabetical order',
        'list': 'a place to store elements',
        'condition': 'put something into special treatment starting with '
                    'if function',
        }

for term, meaning in glossary.items():
    print(f"{term.title()}: {meaning}.\n")