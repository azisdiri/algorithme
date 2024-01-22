from numpy import array
def remplir(M,n):
    for i in range(n):
            M[0,i] = i+1
    for l in range(1,n):
        for c in range(0,n-l):
            M[l,c] = M[l-1,c] + M[l-1,c+1]

#programme principal
n = int(input('donner n : '))
while not (n>0):
    n = int(input('erreur donner n : '))
M = array([[int()]*n]*n)
remplir(M,n)
print(M)