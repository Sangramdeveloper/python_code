L1=[[1,2,3],[4,5,6],[7,8,9]]
L2=[]
for i in range(len(L1)):
    x=[]
    for j in range(len(L1)):
        if i<=j:
            x.append(L1[i][j])
        L2.append(x)
print(L2)
