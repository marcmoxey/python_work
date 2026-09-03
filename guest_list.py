guests = ['YE', 'Lucki','Jay-z']
message = f"I would like to invite you {guests[0]} to dinner"
print(message)
message = f"I would like to invite you {guests[1]} to dinner"
print(message)
message = f"I would like to invite you {guests[-1]} to dinner"
print(message)
guest_count = len(guests)
print(f"I am invite {guest_count} guest")
print()


# Changing Guest List 
print(f'{guests[-1]} can not make it to dinner')
not_going = 'Jay-z'
guests.remove(not_going)
guests.append('Future')
message = f"I would like to invite you {guests[0]} to dinner"
print(message)
message = f"I would like to invite you {guests[1]} to dinner"
print(message)
message = f"I would like to invite you {guests[-1]} to dinner"
print(message)
guest_count = len(guests)
print(f"I am invite {guest_count} guest")
print()

# More Guest 
print('I found a bigger table')
guests.insert(0, 'Jessica Alba')
guests.insert(3, 'Playboi Catri')
guests.append('lil Uzi Vert')
message = f"I would like to invite you {guests[0]} to dinner"
print(message)
message = f"I would like to invite you {guests[1]} to dinner"
print(message)
message = f"I would like to invite you {guests[2]} to dinner"
print(message)
message = f"I would like to invite you {guests[3]} to dinner"
print(message)
message = f"I would like to invite you {guests[-1]} to dinner"
print(message)
guest_count = len(guests)
print(f"I am invite {guest_count} guest")
print()

# Shrinking Guest List 
print('Can only invite two people')
uninvited_guest = guests.pop()
message = f"Sorry can't invite {uninvited_guest} to dinner"
print(message)
uninvited_guest = guests.pop()
message = f"Sorry can't invite {uninvited_guest} to dinner"
print(message)
uninvited_guest = guests.pop()
message = f"Sorry can't invite {uninvited_guest} to dinner"
print(message)
uninvited_guest = guests.pop()
message = f"Sorry can't invite {uninvited_guest} to dinner"
print(message)
print()
message = f"{guests[0]} you are still invited to dinner"
print(message)
message = f"{guests[-1]} you are still invited to dinner"
print(message)
guest_count = len(guests)
print(f"I am invite {guest_count} guest")

print()
del guests[0]
del guests[-1]
print(guests)
