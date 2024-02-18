t = [5,3,10,2,15,8,9]
n = 7
#decalage a dte methode 1
aux = t[n-1]
for i in range(n-1,0,-1):
    t[i] = t[i-1]
t[0] = aux
print(t)
#decalage a dte methode 2
aux1 = t[n-1]
for j in range(n-2,-1,-1):
    t[j+1] = t[j]
t[0] = aux1
print(t)
#decalage a gauche methode 1
aux2 = t[0]
for k in range(0,n-1):
    t[k] = t[k+1]
t[n-1] = aux2
print(t)
#decalage a gauche methode 2
aux3= t[i]
for l in range(1,n):
    t[l-1] = t[l]
t[n-1] = aux
print(t)
