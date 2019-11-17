def make_shirt(message='I love Python', size='large'):
    """
    Display a summarize of a user orders a t-shirt,
    includes size & message on t-shirt.
    """
    order = f"--- A user ordered a {size} t-shirt "
    order += f"with the following message:\n\t{message}"

    print(order)
    print("")

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'The Computer Scientiest')