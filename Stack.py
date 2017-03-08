s=input("Enter the expression : ")
stack=[]
for i in s.split(' '):
    if i in ['+','-','/','*']:
        m=stack.pop()
        n=stack.pop()
        if i=='-':
            result=m-n
        if i=='+':
            result=m+n
        if i=='*':
            result=m*n
        if i=='/':
            result=m/n
        stack.append(result)
    else:
        stack.append(int(i))
    print(stack)
print(stack.pop())
