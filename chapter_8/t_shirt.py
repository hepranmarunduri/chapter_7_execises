def make_shirt(size, message):
    """
    Display a summarize of a user orders a t-shirt,
    includes size & message on t-shirt.
    """
    order = f"--- A user ordered a {size}-inches t-shirt "
    order += f"with following message:\n\t{message}"

    print(order)
    print("")
    

# Call the function with positional argument.
make_shirt('large', 'The Computer Scientist')

# Call the function with keyword argument.
make_shirt(message='SCREAM!!!', size='medium')