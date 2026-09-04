favorite_number = 00 
print(f"My favorite number is {favorite_number}")


favorite_numbers = {
    'marc' : {
        'numbers' : [0,1]
    },
        'nio' : {
        'numbers' : [4,6,8]
    },
        'jon' : {
        'numbers' : [12]
    },
}

for person, num in favorite_numbers.items():
    if  len(num['numbers']) <= 1:
        print(f"{person.title()} favorite number is: \n{num['numbers']}")
    else:
         print(f"{person.title()} favorite numbers are: \n{num['numbers']}")