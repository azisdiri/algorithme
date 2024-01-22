'''def W():
    p =  1
    for  i in range(1,n+1):
        p=p+2*(i+1)
    return p
n = int(input('donner n : '))
print(W())    
    '''
def W(p,i):
    if i>n:
        return p
    else:
        return W(p+2*(i+1),i+1)
    
n = int(input('donner n : '))
print(W(1,1))   
