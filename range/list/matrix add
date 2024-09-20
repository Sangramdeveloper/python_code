matrix add
_______________
L1=[[1,2,3],[4,5,6]]
L2=[[2,1,3],[1,1,1,]]
L3=[]
for i in range(len(L1)):
	x=[]
	for j in range(len(L1[i])):
		x.append(L1[i][j]+L2[i][j])
	L3.append(x)
print("after add elements are")
print(L3)
C:\Users\DELL\Desktop\pythonprogram>py 1.py
after add elements are
[[3, 3, 6], [5, 6, 7]]




L1=[[1,2,3],[4,5,6]]
L2=[[2,1,3],[1,1,1,]]
L3=[[0,0,0],[0,0,0]]
for i in range(len(L1)):
	for j in range(len(L1[i])):
		L3[i][j]=L1[i][j]+L2[i][j]
print("after add elements are")
print(L3)




C:\Users\DELL\Desktop\pythonprogram>py 1.py
after add elements are
[[3, 3, 6], [5, 6, 7]]


matrix add using list comhershenion
_____________________________________
L1=[[1,2,3],[4,5,6]]
L2=[[2,1,3],[1,1,1,]]
L3=[[L1[i][j]+L2[i][j] for j in range(len(L1[i]))]
for i in range(len(L1))]
print("after add elements are")
print(L3)
C:\Users\DELL\Desktop\pythonprogram>py 1.py
after add elements are
[[3, 3, 6], [5, 6, 7]]



upper triangle

L1=[[1,2,3],[4,5,6],[7,8,9]]
L2=[]
for i in range(len(L1)):
	x=[]
	for j in range(len(L1[i])):
		if i<=j:
			x.append(L1[i][j])
	L2.append(x)
print(L2)

C:\Users\DELL\Desktop\pythonprogram>py 1.py
[[1, 2, 3], [5, 6], [9]]

using list comhershenion
______________________
L1=[[1,2,3],[4,5,6],[7,8,9]]
L2=[[L1[i][j]   for j in range(len(L1[i])) if  i<=j]for i in range(len(L1))]
print(L2)

C:\Users\DELL\Desktop\pythonprogram>py 1.py
[[1, 2, 3], [5, 6], [9]]



lower triangle

L1=[[1,2,3],[4,5,6],[7,8,9]]
L2=[]
for i in range(len(L1)):
	x=[]
	for j in range(len(L1[i])):
		if i>=j:
			x.append(L1[i][j])
	L2.append(x)
print(L2)


diangole


L1=[[1,2,3],[4,5,6],[7,8,9]]
L2=[]
for i in range(len(L1)):
	x=[]
	for j in range(len(L1[i])):
		if i==j:
			x.append(L1[i][j])
	L2.append(x)
print(L2)






L=[[1,2,3],[4,5,6]]
L1=[]
for i in range(len(L[0])):
	x=[]
	for j in range(len(L)):
		x.append(L[j][i])
	L1.append(x)
print(L1)

o/p:
[[1, 4], [2, 5], [3, 6]]


L=[[1,2,3],[4,5,6]]
L1=[[0,0],[0,0],[0,0]]
for i in range(len(L[0])):
		for j in range(len(L)):
			L1[i][j]=L[j][i]
print(L1)

o/p:
[[1, 4], [2, 5], [3, 6]]


L=[[1,2,3],[4,5,6]]
L1=[[L[j][i]for j in range(len(L))]for i in range(len(L[0]))]
print(L1)

o/p:
[[1, 4], [2, 5], [3, 6]]



multification
_______________________
L1=[[1,2,3],[4,5,6]]
L2=[[1,2],[1,2],[2,3]]
L3=[]
for i in range(len(L1)):
	x=[]
	for j in range(len(L2[0])):
		s=0
		for k in range(len(L1[0])):
			s=s+L1[i][k]*L2[k][j]
		x.append(s)
	L3.append(x)
print(L3)


o/p:
[[9, 15], [21, 36]]


L1=[[1,2,3],[4,5,6]]
L2=[[1,2],[1,2],[2,3]]
L3=[[sum([L1[i][k]*L2[k][j] for k in range(len(L1[0]))])for j in range(len(L2[0]))]for i in range(len(L1))]
print(L3)


C:\Users\HP\Desktop\pythonprogram>py 1.py
[[9, 15], [21, 36]]