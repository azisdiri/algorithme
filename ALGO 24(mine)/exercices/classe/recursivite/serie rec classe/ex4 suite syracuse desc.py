'''def syracuse(a,n):
    for i in range(1,n+1):
        if a % 2 == 0 :
            a = a//2
        else:
            a=a*3+1
    return a'''
def syracuse(a,n):
    if n < 1:
        return a
    else:
        if (a%2==0):
            return syracuse(a//2,n-1)
        else:
            return syracuse(a*3+1,n-1)

a=int(input('donner a : '))
n=int(input('donner n : '))
print(syracuse(a,n))