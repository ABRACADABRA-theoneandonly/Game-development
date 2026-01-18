dict={"abcdefghijklmnopqrstuvwxyz":"letters",
"continent":"Antartica",
"dictionary":"GIANT BOOK"}
print (dict)
#access the value with the help of keys
print (dict["dictionary"])
#print all the keys
print (dict.keys())
print (dict.values())
if "keyboard" in (dict):
    print ("UIIA")
else:
    print("keyboard not in dIcTiOnArY...")
#add a new key value to the dictionary
dict["IT"]="Information Technology"
print (dict)
#delete a key value in the dictionary
del(dict["continent"])
print (dict)
#update a value in the dictionary
dict["abcdefghijklmnopqrstuvwxyz"]="alphabet"
print (dict)
#add a list to the dictionary
dict["marks"]=["scribble","lines","zigzag","curvy lines","blended lines","MESSY"]
print (dict)
#access a certain string from the list
print (dict["marks"][3])
