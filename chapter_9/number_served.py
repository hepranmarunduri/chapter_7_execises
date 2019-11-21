class Restaurant:
    """Starts from restaurant.py."""
    
    def __init__(self, restaurant_name, restaurant_type):
        """Add attribute number_served that have default value 0."""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """
        Method shows the resto's info.
        ds = describe restaurant.
        """
        ds = f"{self.restaurant_name.title()} serves {self.restaurant_type} "
        ds += "food."
        print(ds)
        
    def open_restaurant(self):
        """Method indicates the resto's open."""
        print(f"{self.restaurant_name.title()} is open!")
        
    def set_number_served(self, served_customers):
        """
        Add method set_number_served() to set the numbers of, customers who's
        been served.
        sns = set no. served
        """
        self.number_served = served_customers
        sns = "The number of customers has served are "
        sns += f"{self.number_served}."
        
        return sns
        
    def increment_number_served(self, today_customers):
        """
        Add method increment_number_served() to increment, the no. of
        customers who's been served.
        """
        self.number_served += today_customers
        sns = "The number of customers has served are "
        sns += f"{self.number_served}."
        
        return sns
        
# Create an instance from the class.  
restaurant = Restaurant('theresto', 'minang')

print(restaurant.restaurant_name.title())
print(restaurant.restaurant_type)

# Print the no. of customers the restaurant has served.
# Expected output: 0 customers.
print(f"\nThe number of customers has served are {restaurant.number_served}.\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()
print("")

# Call the method with new number and print the value
print(restaurant.set_number_served(80))
print(restaurant.set_number_served(90))

# Call the method to represent how many customers were served in.
# Expected output: 100 customers.
print(restaurant.increment_number_served(10))
