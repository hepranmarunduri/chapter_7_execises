"""
Use a dictionary to store information about a person you know. Store their 
first name, last name, age, and the city in which they live. You should have 
keys such as first_name, last_name, age, and city. Print each piece of 
information stored in your dictionary.
"""

sm = {
    'first_initial': 's',
    'last_initial': 'm',
    'birth': 1964,
    'city': 'padang',
    }

print(f"SM's first name initial is {sm['first_initial'].title()}. "
    f"His last name initial is {sm['last_initial'].title()}.\n"
    f"He was born in {sm['birth']}. "
    f"Now, he lives at {sm['city'].title()}.")

# Expected output:
# SM's first name initial is S. His last name initial is M.
# He was born in 1964. Now, he lives at Padang.