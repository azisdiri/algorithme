def supprimer():
    global n
    print(t)
    p = int(input('donner une position : '))
    for i in range(p,n-1):
        t[i] =  t[i+1]
    n-=1
    
def afficher():
    for i in range(n):
        print(t[i],end="/")
        
#pp
t = [5,3,10,2,15,8,9]
n = 7
supprimer()
afficher()