prompt = "\nEnter a topping for your pizza."
prompt += "\nEnter 'quit' to exit program. "

active = True

while active:
    toppings = input(prompt)
    
    if toppings == 'quit':
        active = False
    else:
        print(f"Added {toppings} to your pizza")