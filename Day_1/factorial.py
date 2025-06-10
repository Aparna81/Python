print("enter a no")
n = int(input())
f=1
i=1
s=1
while(i<=n):
    f=f*i
    i+=1
for j in range(1,n+1):
    s=s*j
print(s)
print(f)