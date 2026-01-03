def rmv(r, i):
    m=len(r)
    u=""
    v=""
    for j in range(m):
        if j<i:
            u=u+r[j]
        elif j>i:
            v=v+r[j]
    r=u+v
    return r

def sm(s,f):
    y=len(f)
    n=0
    for i in range(y):
        s=rmv(s,f[i]-n)
        n=n+1
    return s

def sort_string(s):
    result=""
    n=len(s)
    O=[]
    x=[]
    while len(s)>0:
        print(len(s))
        x.append(s[0])
        k=1
        f=[0]
        for j in range(1,len(s)):
            if s[0]==s[j]:
                f.append(j)
                k=k+1
        O.append(k)
        s=sm(s,f)
    print(x,O)
    while len(O)>0:
        max=O[0]
        indexmax=0
        for j in range(len(O)):
            if O[j]>max:
                indexmax=j
                max=O[j]
        for i in range(max):
            result=result+x[indexmax]
        O.pop(indexmax)
        x=rmv(x, indexmax)
    return result
s='trtryneiaaaaffaaf'
print(sort_string(s))
