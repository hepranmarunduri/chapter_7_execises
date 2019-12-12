# See page 99 for detail instruction.

sm = {
    'first_initial': 's',
    'last_initial': 'm',
    'birth': 1964,
    'city': 'padang',
    }

# msg shorts of message
msg = f"His initial name is {sm['first_initial']}.\n"
msg += f"His last name initial is {sm['last_initial']}.\n"
msg += f"He was born in {sm['birth']}.\n"
msg += f"Now, he lives at {sm['city'].title()}.\n"

print(msg)