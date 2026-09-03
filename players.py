

# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3]) # includes first 3 players 
# print(players[1:4]) # slice starts at index 1 and end at 4
# print(players[:4]) # start list at beginning of the list
# print(players[2:]) # slice starts at 2nd index
print(players[-3:]) # last three players 

# Looping Through a Slice 
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)