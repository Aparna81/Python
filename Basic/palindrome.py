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


'''

Try to Optimize the program

for example

below is the optimized code

s = input("Enter the String")
a = len(s)-1
c=0
for i in s:
    if i != s[a]:
        c+=1
        break
    a-=1
if c==0:
    print("Pallindrome")
else:
    print("Not Pallindrome")

'''
    
