def checkfact():
    print("enter a number")
    no=int(input())
    f=1
      while no>0:
       f=f*no
       no=no-1
       print("factorial",f)
checkfact()