def describe_city(city, country='indonesia'):
    """Display a city with its country."""
    print(f"- {city.title()} is a city located in {country.title()}.")


describe_city('padang')
describe_city('surabaya')
describe_city('kyoto', 'japan')