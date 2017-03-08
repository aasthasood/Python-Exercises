for a in range(1,9,1):
    for p in range(1,10,1):
        for l in range(1,10,1):
            for e in range(0,10,1):
                for m in range(0,10,1):
                    for o in range(0,10,1):
                        for n in range(0,10,1):
                            for b in range(1,10,1):
                                if a!=p and a!=l and a!=e and a!=m and a!=o and a!=n and a!=b and p!=l and p!=e and p!=m and p!=o and p!=n and p!=b and l!=e and l!=m and l!=o and l!=n and l!=b and m!=o and m!=n and m!=b and o!=n and o!=b and n!=b and o!=b:
                                    apple = a*10000+p*1000+p*100+l*10+e
                                    lemon = l*10000+e*1000+m*100+o*10+n
                                    banana = b*100000+a*10000+n*1000+a*100+n*10+a
                                    if apple+lemon == banana :
                                        print(a,p,p,l,e,"+",l,e,m,o,n,"=",b,a,n,a,n,a)
                                    else:
                                        continue
