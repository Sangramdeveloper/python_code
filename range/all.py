print("enter a string ")
s=input()
alp,lw,up,vw,co,dg,sp,wd,c,sy=0,0,0,0,0,0,0,0,0,0
for i in s:
    if i.isalpha():
        alp=alp+1
        if i.isupper():
            up=up+1
        else:
            lw=lw+1
        if i in "aeiouAEIOU":
            vw=vw+1
        else:
            co=co+1
    elif i.isdigit():
        dg=dg+1
    elif i.isspace():
        sp=sp+1
    else:
        sy=sy+1
    c=c+1
wd=sp+1

print("total no of char=",c)
print("total no of alp=",alp)
print("total no of vw=",vw)
print("total no of co=",co)
print("total no of upper=",up)
print("total no of lower=",lw)
print("total no of digit=",dg)
print("total no of space=",sp)
print("total no of sy=",sy)
print("total no of word=",wd)
