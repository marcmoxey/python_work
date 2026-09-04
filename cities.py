cities = {
    'new york' : {
        'population' : 8_584_629, 
        'country' : 'usa',
        'fact' : 'Has the most of the USA GDP'
    },
        'miami' : {
        'population' : 489_812, 
        'country' : 'usa',
        'fact' : ''
    },
        'houston' : {
        'population' : 2_419_191, 
        'country' : 'usa',
        'fact' : '4th biggest population in the usa'
    },
}

for city, city_info in cities.items():
    print(f"{city.title()} has {city_info['population']} and {city_info['fact']}")