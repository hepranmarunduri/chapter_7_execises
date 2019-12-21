filename = 'learning_python.txt'


print("\tRead the entire file.")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)


print("\n\tLoop over the file object.")
with open(filename) as file_object:
    for content in file_object:
        print(content.rstrip())


print("\n\tStore the lines in list.")
with open(filename) as file_object:
    contents = file_object.readlines()

each_content = ''
for content in contents:
    each_content += content

print(each_content)