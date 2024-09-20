no=1218
os=0
es=0
while no!=0:
    r=no%10
    if r%2==0:
      es=es+r
    else:
      os=os+r
no=no//10
print("sum of odd digit=",os)
print("sum of even digit=",es)