#Get 20 random marks for 20 students (between 0 to 100). Create 3 separate empty lists . The first list should contain the marks <=30. The second list between 31 to 69. The third list >= 70.
import random
delta = []  
gamma = []   
beta = []   
standard = [random.randint(0, 100) for i in range(20)]
for mark in standard:
    if mark <= 30:
        delta.append(mark)
    elif 31 <= mark <= 69:
        gamma.append(mark)
    else:
        beta.append(mark)
print("all:", standard)
print("lowest:", delta)
print("average:", gamma)
print("highest:", beta)