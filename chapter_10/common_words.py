def count_common_words(text, word):
    """Counts similar words in a single text file."""
    try:
        with open(text) as file_object:
            contents = file_object.read()
    except :
        pass
    else:
        count_contents = contents.lower().count(word)
        print(count_contents)

filename = 'the_little_econ.txt'
count_common_words(filename, 'the')