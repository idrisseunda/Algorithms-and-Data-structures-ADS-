Start algo: sTRING

Define:
    s:string;
    n,l,u,i,j:intergers.
    
Initialization:
    input s = 'PLease enter the string of "(",")" and lower english characters'
    n = lenght of s
    l = 0
    u = 0
for i from 0 to n-1 Do
    if s[i]="(" Then
        l=l+1
    else then
        if s[i]= ")" Then
            u=u+1
        end if
    end if
    if u>l Then
        remove s[i] from s
if l=u Then
    return s
else Then
     n = lenght of s
     v=0
     k=0
    if l>u Then
     for i from 0 to n-1 Do
        if s[n-1-i]="(" Then
            v=v+1
        else then
            if s[n-1-i]= ")" Then
                k=k+1
            end if
        end if
        if v>k Then
            remove s[n-i-1] from s
     if v= k Then
        return s   
