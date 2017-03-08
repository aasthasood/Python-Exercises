a = int(input('Endpoint 1 : '))
b = int(input('Endpoint 2 : '))
k=[]
for i in range (a,b+1):
    l=[]
    j = int(i)
    while(i!=l):
        if i%2==0:
            i=i/2
            l.append(int(i))
        else:
            i=3*i+1
            l.append(int(i))
    k.append(len(l)+1)
    print("Cycle Length of",j,"is",len(l)+1);
print("Maximum cycle length is",max(k))
