sandwich_orders = ['chicken','pastrami', 'turkey','pastrami' ,'tuna', 'pastrami']
finished_sandwiches = []


print("The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    order = sandwich_orders.pop()
    finished_sandwiches.append(order)
     
 
print(finished_sandwiches)