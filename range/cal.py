s=input("enter a string")
c=0
for i in s:
	if i.isalpha():
		c=c+1
print("no of alpha =",c)