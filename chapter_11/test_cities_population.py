# Copy from test_cities.py

import unittest
from city_functions_population import get_formatted_city_country_string

class CityCountryTest(unittest.TestCase):
    """Does formatted string like 'Santiago, Chile' work?"""
    def test_formatted_city_country_string(self):
        formatted_string = get_formatted_city_country_string(
            'santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_string = get_formatted_city_country_string(
            'santiago', 'chile', population=5_000_000)
        self.assertEqual(formatted_string, 
            'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()