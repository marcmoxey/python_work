people = {
    'marc' : {
        'first' : 'marc-anthony',
        'last' : 'moxey',
        'age' : 25,
        'location' : 'new york'
    }, 
        'jon' : {
        'first' : 'jonthan',
        'last' : 'martian',
        'age' : 25,
        'location' : 'new york'
    }, 
        'nio' : {
        'first' : 'nio',
        'last' : 'coreas',
        'age' : 25,
        'location' : 'florida'
    }, 
}


for person, person_info in people.items():
    print(f"\nUsername: {person}")
    full_name = f"{person_info['first']} {person_info['last']}"
    location = person_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")