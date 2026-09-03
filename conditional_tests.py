car = 'toyota'

print("Is car == 'toyota'? I predict True.")
print(car == 'toyota')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

car = 'benz'

print("Is car == 'benz'? I predict True.")
print(car == 'benz')

print("Is car == 'bmw'? I predict False.")
print(car == 'bmw')


car = 'lambo'

print("Is car == 'lambo'? I predict False.")
print(car == 'lambo')

print("Is car == 'bmw'? I predict False.")
print(car == 'bmw')

car = 'lexus'

print("Is car == 'lexus'? I predict False.")
print(car == 'lexus')

print("Is car == 'subaru'? I predict False.")
print(car == 'subaru')


car = 'range rover'

print("Is car == 'lexus'? I predict False.")
print(car == 'range rover')

print("Is car == 'bently'? I predict False.")
print(car == 'bently')


print()
motorcycle = 'Honda'
print(motorcycle == 'honda')
print(motorcycle.lower() == 'honda')
print()


age_0 = 16
age_1 = 21

if age_0 == age_1:
    print("You are 21")
    
if age_0 != age_1:
    print("You are not 21")
    
if age_1 > age_0:
    print(f"You have to be {age_1} to enter")

age_0 = 15
age_1 = 16
if age_0 < age_1:
    print(f"You have to be {age_1} to get your permit")
    
    
age_0 = 13

if age_0 >= 13:
    print("You may sign up for this website")
    
age_1 = 24

if age_1 <= 25: 
    print("Your still on your parent insurance")
    
age_0 = 18
age_1 = 16

if age_0 and age_1 >= 17:
    print("You may get your license")
    
    
age_0 = 18
age_1 = 16


if age_0 or age_1 >= 17:
    print("You may get your license")
    
    
cars = ['bmw', 'benz', 'audi', 'volkswagon', 'porch']


reilable_car = 'toyota'
if reilable_car not in cars:
    print(f"{reilable_car} is not a german car")
    
car = 'bmw'

if car in cars:
    print(f"{car} was made in germany")