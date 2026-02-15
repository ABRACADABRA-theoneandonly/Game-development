groups=[]
for i in range(5):
    user = input("What's your group name? ")
    user1 = input("What's the size of the group? ")
    user2 = input("What's the date of the competition? ")
    user3 = input("What's the venue? ")
    user4 = input("What's the type of medal? ")
    groupinfo= (user,user1, user2, user3, user4)
    groups.append(groupinfo)
print(groups)