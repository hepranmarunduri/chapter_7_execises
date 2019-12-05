"""
Make a dictionary called cities. Use the names of three cities as keys in your 
dictionary. Create a dictionary of information about each city and include the 
country that the city is in, its approximate population, and one fact about 
that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the 
information you have stored about it.
"""
cities = {
    'padang': {
        'country': 'indonesia',
        'population': 833_562,
        'fact': 'The capital city of Sumatera Barat',
        },

    'surabaya': {
        'country': 'indonesia',
        'population': 2_765_000,
        'fact': 'The capital city of Jawa Timur.',
        },

    'mecca': {
        'country': 'saudi arabia',
        'population': 1_535_000,
        'fact': 'Where masjid al-haram is.',
        },
    }

# Show all information within the dictionaries
for city_name, cities_info in cities.items():
    country = cities_info['country'].title()
    population = cities_info['population']
    fact = cities_info['fact']

    print(f"City          : {city_name.title()}\n"
        f"Country       : {country}\n"
        f"Population    : {population}\n"
        f"Fact          : {fact}\n")