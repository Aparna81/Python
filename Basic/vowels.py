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

'''
s is already in the type of 'string'

there is no need to put like 'str(s[i])' instead write 's[i]'

try to use 'in' keyword

s = input('Enter the string')
n = 'aeiou'
count = 0
for i in s:
    if i in n:
        count+=1
print(f' The vowels count is {count}')
    

'''
