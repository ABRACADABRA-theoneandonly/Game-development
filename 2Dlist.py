matrix=int(input("Enter the row"))
matrix1=int(input("Enter the column"))
matrix100=[]
for i in range(matrix):
    ooooo=[]
    for o in range(matrix1):
        user=int(input("Enter the element"))
        ooooo.append(user)
    matrix100.append(ooooo)
for u in range(matrix):
    for y in range(matrix1):
        print(matrix100[u][y],end=" ")
    print()
matrix34=[[100,7,80],[123,4,2]]
matrix45=[[1,2,3],[1,9,6]]
matrixadd=[[0,0,0],[0,0,0]]
matrixsub=[[0,0,0],[0,0,0]]
for t in range(2):
    for r in range(3):
        matrixadd[t][r]=matrix34[t][r]+matrix45[t][r]
        matrixsub[t][r]=matrix34[t][r]-matrix45[t][r]
        print(matrixadd[t][r],end=" ")
        print(matrixsub[t][r],end=" ")
    print()