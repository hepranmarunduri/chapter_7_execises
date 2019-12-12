class Restaurant():
    """Models a restaurant."""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Displays restaurant name & its cuisine type."""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Displays the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open.")

    def set_number_served(self, number_served):
        """Sets the number of customers that have been served."""
        self.number_served = number_served
        return self.number_served

    def increment_number_served(self, number_served_in_a_day):
        """Increments the number of customers who's been served in a day."""
        self.number_served += number_served_in_a_day
        return self.number_served
        

restaurant = Restaurant('canteen', 'prasmanan', 122)

print(restaurant.number_served)

print(restaurant.set_number_served(5151))

print(restaurant.increment_number_served(10))
print(restaurant.increment_number_served(11))
print(restaurant.increment_number_served(12))