
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

def sm(a,b):
    y=len(b)
    m=0
    for i in range(y):
        a=rmv(a,b[i]-m)
        m=m+1
    return s

def strg(s):
    n = len(s)
    u = 0
    v=0
    k=0
    l=0
    z=list()
    for i in range(n):
        if s[i]=="(":
            l=l+1
        elif s[i]== ")":
            u=u+1
        if u>l:
            z.append(i)
            u=u-1
    if l==u :
      s=sm(s,z)
      return s
    else :
     n = len(s)
     z=list()
     if l>u :
      for i in range(n):
        if s[n-1-i]=="(":
            v=v+1
        else :
            if s[n-1-i]== ")":
                k=k+1
        if v>k :
            z.append(n-i-1)
            v=v-1
     if v==k:
        s=sm(s,z)
        return s   
s="))(())dhefrwedj)hdcbdh)jdc nh)kjdncjd(ckwje) cjw)"
print(strg(s))