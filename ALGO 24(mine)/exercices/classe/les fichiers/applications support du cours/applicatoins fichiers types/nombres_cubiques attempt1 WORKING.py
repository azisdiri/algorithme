from pickle import *
def saisir():
    global n 
    n = int(input('donner n : '))
    while not (4<=n<=20):
        n = int(input('donner n : '))
    
def cubique(x):
    ch = str(x)
    a = int(ch[0])
    b = int(ch[1])
    c = int(ch[2])
    return x == a*a*a + b*b*b + c*c*c
    

def remplir():
    global f
    f = open("Nombres.dat",'wb')
    for i in range(n):
        x = int(input('entier n° '+str(i)+" :  "))
        while not(100<=x<=999 ):
            x = int(input('erreur entier n° '+str(i)+" :  "))
        dump(x,f)
    f.close()
        
def afficher():
    f = open("Nombres.dat",'rb')
    print('les entiers cubiques sont : ')
    ok = False
    i = 0
    while not ok:
        try:
            i += 1
            x = load(f)
            if cubique(x):
                print(x,'son ordre : ',i)
        except:
            ok = True
    f.close()
    
saisir()
remplir()
afficher()