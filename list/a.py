L=[]
print("enter how many  list store ")
r=int(input())
for i in range(r):
	x=[]
	print("list ",i+1," store how many data")
	c=int(input())
	for j in range(c):
		print("enter data ",j+1)
		x.append(int(input()))
	L.append(x)
print("elements are ")
print(L)