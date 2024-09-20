print("A")
for i in range(5):
	print("B")
	print(i)
	if i>=2:
		continue
	print("C")
print("D")
print(i)

o/p
A 
B
0
c 
B 
1
C 
B
2
B
3
B
4
D 
4