# See page 78 for detail instruction.

# equality
language = 'bahasa indonesia'
print(language == 'bahasa indonesia') # True
print(language == 'Bahasa Indonesia') # False
# inequality
print(language != 'english') # True
print(language != 'bahasa indonesia') # False
print("")

# Using lower method
brand = 'BMW'
print(brand.lower() == 'bmw') # True
print(brand.lower() == 'toyota') # False
print("")

# Numerical tests
today = 26

print(today == 26) # True
print(today == 27) # False
print(today != 27) # True
print(today != 26) # False
print(today > 10) # True
print(today > 100) # False
print(today < 100) # True
print(today < 10) # False
print(today >= 26) # True
print(today >= 100) # False
print(today <= 26) # True
print(today <= 10) # False
print("")

# Multiple conditions
first_name = 'sherlock'
last_name = 'holmes'

print(first_name == 'sherlock' and last_name == 'holmes') # True
print(first_name == 'sherlock' and last_name == 'conan') # False

# True even last_name is false
print(first_name == 'sherlock' or last_name == 'conan')
print(first_name == 'arthur' or last_name == 'conan') #False
print("")

# Check value in the list
member = ['sukjin', 'jaesok', 'jongkook', 'haha', 'jihyo', 'kwangso', 'somin',
'sechan']

print('sechan' in member) # True
print('gary' in member) # False

print('gary' not in member) # True
print('somin' not in member) # False