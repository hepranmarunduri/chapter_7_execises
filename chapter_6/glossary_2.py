"""
Now that you know how to loop through a dictionary, clean up the code from 
Exercise 6-3 (page 99) by replacing your series of print() calls with a loop 
that runs through the dictionary’s keys and values. When you’re sure that your 
loop works, add five more Python terms to your glossary. When you run your 
program again, these new words and meanings should automatically be included 
in the output.
"""

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
    'condition': 'put something into special treatment starting with if function',
    }

for term, meaning in glossary.items():
    print(f"{term.title()}: {meaning}.\n")