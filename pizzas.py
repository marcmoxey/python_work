pizzas = ['cheese', 'pepperoni','buffalo']

for pizza in pizzas:
    print(f"I like {pizza} pizza")
    
print("I really love pizza")


# Store information about a pizza being ordered 
pizza = {
    'crust' : 'thick',
    'toppings':['mushrooms', 'extra cheese']
}

# Summarize the order 
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")