print("enter the end range")
n=int(input())
def fibo(a,b,c,n):
    if c==n:
        return
    print(a)
    fibo(b,a+b,c+1,n)

    
fibo(0,1,0,n)