prompt = "\nTell me something, and I will repeat it back to you:"
# print(message)

# Letting the User Choose when to Quit 
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# using flags
active = True
while active: 
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)