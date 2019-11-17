def city_country(city, country='indonesia'):
    """Returns a string like 'Padang, Indonesia'."""
    return f"{city.title()}, {country.title()}"

print(city_country('padang'))
print(city_country('surabaya'))
print(city_country('kyoto', 'japan'))
