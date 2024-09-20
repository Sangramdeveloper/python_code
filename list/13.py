L=[]
print("enter list r and c ")
r=int(input())
c=int(input())
print("enter ",r*c,"elements")
for i in range(r):
	x=[]
	for j in range(c):
		x.append(int(input()))
	L.append(x)
print("elements are ")
print(L)