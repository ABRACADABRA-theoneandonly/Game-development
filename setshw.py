#Create 2 sets one for badminton and one for soccer.Use set operations to find:
#Students who play both badminton and soccer. (intersection)
#Students who play either badminton or soccer but not both.(symmetric_difference)
#Students who play only badminton.(difference)
bsets=["ben","larry","will","monkey","triceratops","anna","freddy","xavier","godzilla","grace","eliza"]
badminton=set(bsets)
ssets=["godzilla","steven","chad","stacy","barbie","cocomelon","evil larry","triceratops","ben"]
soccer=set(ssets)
print("there are many people playing soccer and badminton")
print("Would you like to find out who:")
print("1.plays either soccer or badminton but not both")
print("2.plays badminton")
print("3.plays both soccer and badminton")
user=input("please write the number of your choice")
if user =="1":
    print(badminton^soccer)
if user =="2":
    print(badminton-soccer)
if user =="3":
    print (badminton&soccer)
