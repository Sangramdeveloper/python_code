#variable length parameter
#def show(*a):
 #   print(a)
#show(10,12.34)
#show("hii",1,5,3)

def show(b=0,c=7,d=5,*a):
    print(b,c,d)
    print(a)
show(10,12.34)
show("hi",1,5,3)
show(5)
show(1,2,3,4,5,6)