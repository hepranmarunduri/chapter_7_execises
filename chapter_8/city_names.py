def city_country(city, country='indonesia'):
    """
    Return a string formatted like this:
    "City, Country"
    """
    return f"{city.title()}, {country.title()}"


print(city_country('padang'))
print(city_country('surabaya'))
print(city_country('kyoto', 'japan'))