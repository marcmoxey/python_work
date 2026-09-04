pets = {
    'sonic' : {
        'animal' : 'hedgehog',
        'color': 'blue', 
    },
        'shadow' : {
        'animal' : 'hedgehog',
        'color': 'black/red', 
    },
        'tails' : {
        'animal' : 'fox',
        'color': 'orange', 
    },
        'silver' : {
        'animal' : 'hedgehog',
        'color': 'silver', 
    },
        'rouge' : {
        'animal' : 'bat',
        'color': 'white/black/pink', 
    },
        
}

for pet, pet_info in pets.items():
    # print(f"{pet.title()}")
    features = f"{pet_info['color']} {pet_info['animal']}"
    print(f"{pet.title()} is {features}")
    
    