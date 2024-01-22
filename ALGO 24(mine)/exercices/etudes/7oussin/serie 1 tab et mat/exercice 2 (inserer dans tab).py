t = [5,3,10,2,15,8,9]
n = 7

def inserer():
    x = int(input('donner x : '))
    p = int(input('donner p : '))
    while not (0<=p<=n-1):
            p = int(input('erreur donner p : '))
    for i in range(n-1,p,-1):
        t[i] = t[i-1]
    t[p] = x
#pp
inserer()
print(t)