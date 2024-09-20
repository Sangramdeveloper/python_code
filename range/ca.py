s=input("enter a string")
c=0
for i in s:
	if i.isupper():
		c=c+1
print("no of upper case=",c)