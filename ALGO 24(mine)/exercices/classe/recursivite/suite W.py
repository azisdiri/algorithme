'''def W():
    p =  1
    for  i in range(1,n+1):
        p=p+2*(i+1)
    return p
n = int(input('donner n : '))
print(W())    
    '''


def W(n):
    if n == 0:
        return 1
    else:
        return W(n-1) + 2*(n+1)


n = int(input('donner n : '))
print(W(n))
