# Start from restaurant.py.
# Add a new attribute (number_served) with default value 0.
class Restaurant:
    """Models a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 
        self.number_served = 0

    def describe_restaurant(self):
        """Displays some informations of the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} foods.")

    def open_restaurant(self):
        """Indicates the restaurant is opening."""
        print(f"{self.restaurant_name} is {self.open_restaurant}.")

    def display_served_customers(self):
        """
        Display no. of customers have been served.
        dsc = display no. customers
        """
        dsc = f"The no. of customers for today are {self.number_served}."
        return dsc

    def set_number_served(self):
        """Set the number of customers who's been served."""
        self.number_served = 100

        # ns - no. served
        ns = f"There are {self.number_served} customers for today."
        print(ns)

    def increment_number_served(self, new_number_served):
        """Increments the no. of customers who's been served."""
        self.number_served += new_number_served

        # ins = increment no. served
        ins = f"There are {self.number_served} customers for today."
        print(ins)


# Create an instance (restaurant).
restaurant = Restaurant('rm lamun gelombang', 'minang')

# Show the no. of customers the restaurant has served.
restaurant.number_served = 22
print(restaurant.display_served_customers())

# Call set_number_served() method and print the value.
restaurant.set_number_served()

# Represent how many customers were served in.
restaurant.increment_number_served(8)