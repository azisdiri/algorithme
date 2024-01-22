def saisir():
    global n
    n = int(input('donner n : '))
    while not(n>=3):
        n = int(input('err donner n : '))
        
def suite(n):
    x =3
    if n%2 == 0 :
        for i in range(1,n+1):
             x = x//2
        return x
    else:
        for i in range(1,n+1):
            x = x*3+1
        return x
saisir()
print(suite(n))