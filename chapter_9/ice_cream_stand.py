class Restaurant():
    """Models a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays restaurant name & its cuisine type."""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Displays the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open.")


class IceCreamStand(Restaurant):
    """Ice cream stand is a specific kind of restaurant."""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_ice_cream_flavors(self):
        """Display the ice cream flavors in the list."""
        print("Ice cream flavors:")
        for ice_cream_flavor in self.flavors:
            print(f"- {ice_cream_flavor.title()}")
            

flavors_list = ['yakult', 'oreo', 'durian', 'vanilla']

flavor = IceCreamStand('eskrim', 'ice cream', flavors_list)

flavor.display_ice_cream_flavors()