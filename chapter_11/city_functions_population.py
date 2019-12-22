# Copy from city_functions.py

def get_formatted_city_country_string(city, country, population=''):
    """
    Return a formatted string of city and country.
    Like: Santiago, Chile
    """
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"