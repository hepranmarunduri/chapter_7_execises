class Restaurant:
    """Class models a restaurant."""
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        
    def describe_restaurant(self):
        """Method shows the resto's info. ds = describe restaurant."""
        ds = f"{self.restaurant_name.title()} serves {self.restaurant_type} "
        ds += "food."
        print(ds)
        
    def open_restaurant(self):
        """Method indicates the resto's open."""
        print(f"{self.restaurant_name.title()} is open!")

class IceCreamStand(Restaurant):
    """Models an ice cream stand that a part of the restaurant."""
    def __init__(self, restaurant_name, restaurant_type):
        """
        The stand offers several ice cream flavors.
        NOTE: The 'restaurant_name & restaurant_type' are a must included
        parameters in parent & child init methods.
        """
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = ('choco', 'durian', 'strawberry','vanilla')

    def display_flavors(self):
        """Display each ice cream flavors. msg shorts for message."""
        msg = f"Besides {icecream_stand.restaurant_type} culinary, "
        msg += f"{icecream_stand.restaurant_name.title()} also has an ice "
        msg += f"cream stand.\nThe stand offers several ice cream flavors, "
        msg += "which are:"
        
        print(msg)
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


icecream_stand = IceCreamStand('theresto', 'minang')

icecream_stand.display_flavors()