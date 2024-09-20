s=input("enter a string")
vw=0
for i in s:
	if i in "aeiouAEIOU":
		vw=vw+1
print("no of vowel =",vw)