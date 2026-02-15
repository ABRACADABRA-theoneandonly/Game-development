#setssss
sets=[123678,12345678,2345678,345678,45678,5678,678,78,8,123678]
setssssssssss=set(sets)
print(setssssssssss)
#sets are not indexable
#print(setssssssssss[0])
if 5 in setssssssssss:
    print("Number found!")
else:
    print("Errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
arr=set([])
arr.add("OoMpA LoOmPa")
arr.add("helloooooo")
arr.add("qwertyuiopasdfghjklzxcvbnm")
arr.add("qwertyuiopasdfghjklzxcvbnm")
print(arr)
arr.remove("helloooooo")
print(arr)
arr.add("abcdefghijklmnopqrstuvwxyz")
arr.discard("qwertyuiopasdfghjklzxcvbnm")
print(arr)
#Set operations, union
qwe34={1,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,5,5,5,5,5,5,5,5,5}
wer45={9,9,9,9,9,9,9,9,6,6,6,6,1,1,1,1,1,1,6,6,6,6,6,66,6,8,8,8,"9+10=21",3}
print(qwe34.union(wer45))
print (qwe34|wer45)
#intersection
print(qwe34.intersection(wer45))
print (qwe34&wer45)
#Difference
print(qwe34.difference(wer45))
print(qwe34-wer45)
#symmetric difference
print(qwe34.symmetric_difference(wer45))
print(qwe34^wer45)