def primeNumber(num):
    h=1;
    for i in range(2,num):
        if num%i==0:
            h=0
            break
    if h==1:
        return True
num=int(input('Enter a number : '))
print('The prime factors of number',num,'are : ')
for i in range(2,num+1):
    if num%i==0:
        if primeNumber(i):
            print(i)
