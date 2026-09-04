favorite_places = {
    'marc' : {
        'place' : 'spain'
    },
        'nio' : {
        'place' : 'japan'
    },
        'jon' : {
        'place' : 'colombia'
    },
}


for person, place in favorite_places.items():
    print(f"{person.title()} favorite place is {place['place']}")