favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah favorite language is {language}")


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
# Looping Through All the Keys in a Dictionary

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title()) 

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, i see you love {language}!")
        
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
    
# Looping Through a Dictionary's Keys in a Particular Order

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")
    
    
# Looping through All Values in a dictionary 
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"{language.title()}")
    
print()

should_take_poll = ['marc', 'josh', 'sarah', 'phil']

for person in should_take_poll:
    if person in favorite_languages.keys():
        print(f'Thank you for responding {person}')
    else:
        print(f'Please take the poll {person}')
        
        
        
favorite_languages = {
    'jen' : ['python', 'rust'],
    'sarah' : 'c',
    'edward' : ['rust', 'go'],
    'phil' : ['python','haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")