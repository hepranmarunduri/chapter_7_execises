# Exercise 11-1

import unittest

from city_functions import get_formatted_city_country_string

class CityCountryTest(unittest.TestCase):
    """Does formatted string like 'Santiago, Chile' work?"""
    def test_formatted_city_country_string(self):
        formatted_string = get_formatted_city_country_string(
            'santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()