def Dist(i,j):
    if (i==1 and j==2 )or (i==2 and j==1):
        return(cities[0])
    if (i==1 and j==3) or (i==3 and j==1):
        return(cities[1])
    if (i==1 and j==4) or (i==4 and j==1):
        return(cities[2])
    if (i==2 and j==3) or (i==3 and j==2):
        return(cities[3])
    if (i==2 and j==4) or (i==4 and j==2):
        return(cities[4])
    if (i==3 and j==4) or (i==4 and j==3):
        return(cities[5])
cities=[]
temp=9999999;d=0
for i in range(1,5):
    for j in range(i+1,5):
        print("Enter distance between city ",i," and ",j);
        cities.append(int(input()))
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                L=[a,b,c,d]
                if (len(set(L)))==4:
                    d=Dist(a,b)+Dist(b,c)+Dist(c,d)+Dist(d,a)
                    if d<temp:
                        temp=d
                        A,B,C,D=a,b,c,d
print(A,B,C,D,A)
print(temp)
