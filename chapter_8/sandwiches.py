def make_sandwich(*sandwich_items):
    """
    This stores as many as possible item that a user wants on a sandwich.
    """
    for sandwich_item in sandwich_items:
        print(f"Adding {sandwich_item}...")

    print(f"\nHere is your sandwich:{sandwich_items}")
    print("Thank you!\n\n")


make_sandwich('black pepper')
make_sandwich('grilled meat', 'tomato')
make_sandwich('rendang', 'dendeng', 'nasi bungkus')