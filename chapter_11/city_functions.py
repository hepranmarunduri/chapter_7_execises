# Exercise 11-1

def get_formatted_city_country_string(city, country):
    """
    Return a formatted string of city and country.
    Like: Santiago, Chile
    """
    return f"{city.title()}, {country.title()}"