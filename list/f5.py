#reurn value with no arguments
def check()
    print("enter two number")
    no1=int(input())
    if no%2==0:
        return True
    else:
        return False
if check():
    print("even number")
else:
    print("odd number")