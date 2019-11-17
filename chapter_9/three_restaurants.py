class Restaurant:
    """Models a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name                  # Attribut 1
        self.cuisine_type = cuisine_type                        # Attribut 2

    def describe_restaurant(self):                              # Method 1
        """Displays some informations of the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} foods.")

    def open_restaurant(self):                                  # Method 2
        """Indicates the restaurant is opening."""
        print(f"{self.restaurant_name} is {self.open_restaurant}.")


lamun_gelombang = Restaurant('RM Lamun Gelombang', 'minang')
afoodrica = Restaurant('Afoodrica Restaurant', 'african')
eurofood = Restaurant('Euroofood Resto', 'western')


afoodrica.describe_restaurant()
lamun_gelombang.describe_restaurant()
eurofood.describe_restaurant()