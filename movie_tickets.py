prompt = "\nEnter your age for the price of the movie ticker."
prompt += "\nEnter 'quit' to exit program.: "

active = True 
while active:
    age_str = input(prompt)
    
    if age_str == 'quit':
        break
    
    else: 
        age = int(age_str)
        if age <= 3:
            ticket = 0
            print(f"The ticket is ${ticket} for person under 3")
        elif age > 3 and age <= 12:
            ticket = 10
            print(f"The ticket is ${ticket} for person between age 3 and 12")
        elif age > 12:
            ticket = 15
            print(f"The ticket is ${ticket} for person over the age 12")
    

    
    
    
        