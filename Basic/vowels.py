print("enter a string")
s=input()
n="aeiou"
i=0
c=0
while(i<len(s)):
    j=0
    while(j<len(n)):
        if str(s[i])==str(n[j]):
            c=c+1
        j+=1
    i+=1
print(c)