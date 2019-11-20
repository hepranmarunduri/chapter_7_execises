# This program starts from restaurant.py

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
        
# Create 3 different instances
lamun_gelombang = Restaurant('RM Lamun Gelombang', 'minang')
afoodrica = Restaurant('Afoodrica Restaurant', 'african')
eurofood = Restaurant('Euroofood Resto', 'western')

# Call describe_restaurant() for each instance.
afoodrica.describe_restaurant()
lamun_gelombang.describe_restaurant()
eurofood.describe_restaurant()
