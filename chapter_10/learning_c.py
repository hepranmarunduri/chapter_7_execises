# Replace word 'Python' with 'C'

filename = 'learning_python.txt'

with open(filename) as file_object:   
    contents = file_object.read()

# Don't necessary to type 'print(contents)'
print(contents.replace('python', 'C'))