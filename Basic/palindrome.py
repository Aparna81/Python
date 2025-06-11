print('enter the string')
s=input()
c=0
a=len(s)-1
for i in s:
    if str(i) != str(s[a]):
          c+=1
    a-=1
if(c==0):
    print("palidrome")
else:
    print("not palindrome")