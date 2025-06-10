print("start and end range")
n = int(input())
m = int(input())
#i=2
#c=0       check prime or not for a no
#while(i<n):
 #   if(n%i==0):
  #      c+=1
   # i=i+1
#if(c==0):
 #   print("it is a prime no" + str(i))
#else:
 #   print("not prime")
for i in range(n,m+1):
    j=2
    c=0
    while(j<i):
        if(i%j==0):
            c+=1
        j+=1
    if(c==0):
        print(i)
