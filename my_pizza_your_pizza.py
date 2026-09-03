pizzas = ['cheese', 'pepperoni','buffalo']
friend_pizzas = pizzas[:]
# print(friend_pizza)
pizzas.append("pineapple")
friend_pizzas.append('mushrooms')

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}")
    
print()

for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are: {pizza}")