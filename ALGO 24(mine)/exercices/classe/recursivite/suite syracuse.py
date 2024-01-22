'''def syracuse(x,n):
    for i in range(1,n+1):
        if x % 2 == 0 :
            x = x//2
        else:
            x=x*3+1
    return x'''
def syracuse(x,n):
    if n < 1:
        return x
    else:
        if (x%2==0):
            return syracuse(x//2,n-1)
        else:
            return syracuse(x*3+1,n-1)
    
x=int(input('donner x : '))
n=int(input('donner n : '))
print(syracuse(x,n))

