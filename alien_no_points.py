# Using get() to Access Values 
    # sets a default value that will be return 
alien_0 = {'color': 'green', 'speed':'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)