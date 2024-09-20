L1=[[1,2,3],[4,5,6]]
L2=[[2,1,3],[1,1,1]]
L3=[[L1[i][j]+L2[i][j] for j in range (len(L1[i]))] for i in range (len(L1))]
print("after add elements are")
print(L3)
