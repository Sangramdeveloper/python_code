L1=[[1,2,3],[4,5,6]]
L2=[[2,1,3],[1,1,1]]
L3=[[0,0,0],[0,0,0]]
for i in range (len(L1)):
    for j in range(len(L1[i])):
        L3[i][j]=L1[i][j]+L2[i][j]
print("after add elements are")
print(L3)