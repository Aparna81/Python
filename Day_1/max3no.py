print("enter first, second, third no")
a=int(input())
b=int(input())
c=int(input())
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)
if (a>b) and (a>c):
    print(a)
elif (b>a) and (b>c):
    print(b)
else:
    print(c)