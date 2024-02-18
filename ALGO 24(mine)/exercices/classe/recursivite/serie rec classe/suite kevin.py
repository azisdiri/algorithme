def kev(k0,k1,i):
    if i>n:
        return k0+k1
    else:
        return kev(k1,k0+k1,i+1)
    
k0=input('donner k0 : ')
k1=input('donner k1 : ')
n = int(input('donner n : '))
print(kev(k0,k1,2))