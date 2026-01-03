# Compare the position of two characters and give the indice the one which appear first in the alphabet

def rankalph(x,i,j):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    n=len(alphabet)
    id1=0
    id2=0
    for k in range(n):
        if x[i]==alphabet[k]:
            id1=k
            break
    for k in range(n):
        if x[j]==alphabet[k]:
            id2=k
    if id1>=id2:
        return j
    else:
        return i
    
# Remove the element r[i] from the string r

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

# Remove in s all elements whose indices are in f
def sm(s,f):
    y=len(f)
    n=0
    for i in range(y):
        s=rmv(s,f[i]-n)
        n=n+1
    return s

# Identify the composition of a string 

def sort_string(s):
    result=""
    n=len(s)
    O=[]
    x=[]
    while len(s)>0:
        #print(len(s))
        x.append(s[0])
        k=1
        f=[0]
        for j in range(1,len(s)):
            if s[0]==s[j]:
                f.append(j)
                k=k+1
        O.append(k)
        
        # Remove elements already counted
        s=sm(s,f)
    #print(x,O)
    
    while len(O)>0:
        max=O[0]
        indexmax=0
        for j in range(len(O)):
            if O[j]>max:
                indexmax=j
                max=O[j]
            elif O[j]==max:
                
                # Choose the indexmax according to the alphabetic order
                indexmax=rankalph(x,j,indexmax)
        for i in range(max):
            result=result+x[indexmax]
        O.pop(indexmax)
        x=rmv(x, indexmax)
    return result

# Main function

def String_permut(s1,s2):
    n = len(s1)
    m = len(s2)

    if n>m:
        return False
    else:
        i=0
        k=0
        while m-i-n>=0:
            if sort_string(s1)==sort_string(s2[i:n+i]):
                k+=1
                break
            i+=1
        if k>0:
            return True
        else:
            return False
s1="erttgfuu"
s2="fjbrhrhgrtftuyrte"
print(String_permut(s1,s2))

