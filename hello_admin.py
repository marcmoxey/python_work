
usernames = ['shadvonic', 'shadic', 'dos75', 'admin', 'user']

# usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"{user}, would you like to see a status report")
        else:
            print(f"Greetings {user}")
else:
    print("You have no users")
        
current_users = usernames[:]
# print(current_users)
new_users = ['Shadvonic','Shadic', 'razzy', 'view', 'verticade']

for new_user in new_users:
    if new_user.lower()  in current_users:
        print(f"{new_user} already taken")
    else:
        print(f"{new_user} is available")