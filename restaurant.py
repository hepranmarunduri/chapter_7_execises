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
        
        
restaurant = Restaurant('theresto', 'minang')

# Print the 2 attributes individually.
print(resto.restaurant_name)
print(resto.restaurant_type)

# Call both methods.
resto.describe_restaurant()
resto.open_restaurant()
