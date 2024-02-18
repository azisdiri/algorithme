def syracuse(a,n,i):
    if i>1:
        return a
    else:
        if (a%2==0):
            u = a//2
        else:
            u = a*3+1
        return syracuse(u,n,i+1)

a=int(input('donner a : '))
n=int(input('donner n : '))
print(syracuse(a,n,0))
