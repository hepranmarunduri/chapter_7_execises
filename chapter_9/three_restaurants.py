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
        

restaurant = Restaurant('canteen', 'prasmanan')
cat = Restaurant('cat cafe', 'food for cat')
gold_fish = Restaurant('gold fishy', 'food for fish')

restaurant.describe_restaurant()
cat.describe_restaurant()
gold_fish.describe_restaurant()