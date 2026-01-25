dict={}
while True:
    print ("1.Insert")
    print ("2.Display all countries")
    print("3.Display alll capitals")
    print("4.Get capital")
    print("5.Delete")
    user=input("ENter Your ChOice!!!")
    if user == "1":
        country=input("Enter country name!")
        capital=input("Enter capital name!")
        dict[country]=capital
        print("Country added!")
    elif user == "2":
        print (dict.keys())
    elif user == "3":
        print (dict.values())
    elif user =="4":
        country=input("Enter country name!")
        print (dict[country])
    elif user == "5":
        country=input("Enter country name!")
        del(dict[country])
