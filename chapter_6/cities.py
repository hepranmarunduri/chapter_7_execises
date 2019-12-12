# See page 112 for detail instruction.

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

for city_name, cities_info in cities.items():
    country = cities_info['country'].title()
    population = cities_info['population']
    fact = cities_info['fact']

    print(f"City          : {city_name.title()}\n"
        f"Country       : {country}\n"
        f"Population    : {population}\n"
        f"Fact          : {fact}\n")