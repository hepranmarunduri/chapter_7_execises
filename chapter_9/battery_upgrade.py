class Car:
    """Models a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def increment_odometer(self, mileage):
        """Increment car's odometer."""
        self.odometer_reading += mileage

    def update_odometer(self, mileage):
        """
        Set the odometer reading to given mileage value.
        Because the odometer reading is 0, so the mileage can't be less than 0.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def fill_gas_tank(self):
        """Alert that the car need gasoline."""
        print("The car needs gasoline.")

class Battery():
    """Models a battery for an electric car."""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")  

    def get_range(self):
        """There are 2 sizes of battery."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Check the battery size and set the capacity to 100 if it isn't."""
        if self.battery_size != 100:
            self.battery_size = 100
        
class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car does not need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)

# Before upgrade the battery. Expected Output: 260 miles.
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
# After upgrade the battery. Expected Output: 315 miles.
my_tesla.battery.get_range()