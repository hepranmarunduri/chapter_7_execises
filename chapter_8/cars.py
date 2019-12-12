def car_info(manufacturer, model, **options):
    """
    Stores a car information to a dictionary includes:
    manufacturer, model name, and other informations about the car.
    """
    car_info_dict = {
                'manufacturer': manufacturer,
                'model name': model,
                }

    for key, value in options.items():
        car_info_dict[key] = value

    return car_info_dict


car_info_variable = car_info('toyota', 'fortuner',
                            color='black')

print(car_info_variable)