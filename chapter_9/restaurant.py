class Restaurant:
    """Models a restaurant."""
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        
    def describe_restaurant(self):
        """Shows the resto's info. ds = describe restaurant."""
        ds = f"{self.restaurant_name.title()} serves {self.restaurant_type} "
        ds += "food."
        print(ds)
        
    def open_restaurant(self):
        """Indicates that the resto's open."""
        print(f"{self.restaurant_name.title()} is open!")
        
        
restaurant = Restaurant('theresto', 'minang')

# Print the 2 attributes individually.
print(restaurant.restaurant_name)
print(restaurant.restaurant_type)

# Call both methods.
restaurant.describe_restaurant()
restaurant.open_restaurant()
