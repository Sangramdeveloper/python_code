def checkfact():
    print("enter two number")
    no=int(input())
    f=1
    while no>0:
        f=f*no
        no=no-1
    return f
res=checkfact()
print("factorial=",f)
