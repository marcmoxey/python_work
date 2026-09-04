sandwich_orders = ['chicken', 'turkey', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich")
    finished_sandwiches.append(order)
    
    
print(finished_sandwiches)