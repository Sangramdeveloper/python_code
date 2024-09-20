s=input("enter a string")
c=0
for i in s:
	if i.islower():
		c=c+1
print("no of lower case=",c)