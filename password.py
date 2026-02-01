dict={}
while True:
    print ("1.Insert")
    print ("2.Display all names")
    print("3.Display all passwords")
    print("4.Get password")
    print("5.Delete")
    print("6. Change password")
    user=input("Enter your choice!")
    if user == "1":
        name=input("Enter any name/username!")
        password=input("Enter a password!")
        dict[name]=password
        print("Name added!")
    elif user == "2":
        print (dict.keys())
    elif user == "3":
        print (dict.values())
    elif user =="4":
        name=input("Enter a name!")
        print (dict[name])
    elif user == "5":
        name=input("Enter a name to delete!")
        del(dict[name])
    elif user == "6":
        name = input("Enter your username:")
        if name in dict:
            new_password = input("Enter your new password:")
            dict[name] = new_password
            print("Password has changed!")
        else:
            print("Username not found!")