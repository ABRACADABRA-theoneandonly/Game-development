vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
user=input("Enter your string!").lower()
for i in user:
    if i in vowels:
        vowels[i]+=1
print (vowels)
vowelslist=["a","e","i","o","u"]
dict={}
user=input("Enter your string!").lower()
for i in user:
    if i in vowelslist:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
print (dict)