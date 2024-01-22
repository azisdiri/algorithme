from pickle import dump
n = int(input('donner un entier n: '))
while not(8<=n<=100):
    n = int(input('donner un entier n: '))

def remplir():
    global f
    f = open('nombres.dat','wb')
    for i in range(n):
        x = int(input('donner le nombre n°'+str(i)+" "))
        while not (1<=x<=1000):
            x = int(input('erreur donner le nombre n°'+str(i)+" "))
        dump(x,f)

'''def nombre_occ(T,i):
    nbo = 0
    ok = False
    while not ok:
        try:
            load

        except:'''

def transfert(T,f,n):
    f = open('nombres.dat','rb')
    for i in range(n):
        x = load(f)
        T[i] = x


def creer():
    global fq
    fq = open('frequence.dat','wb')
    T = array([int()]*n)
    transfert(T,f,n)
    for i in range(10):
        e = {}
        e.chiff = i
        e.nbr_occ = nombre_occ(T,i)
        dump(fq,e)
    







#pp