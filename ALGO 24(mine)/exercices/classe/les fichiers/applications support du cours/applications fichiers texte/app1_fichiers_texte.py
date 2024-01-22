from pickle import *
def saisir():
    global f
    f = open("Original.txt","w")
    
    ch = input('donner une chaine : ')
    while ch=='':
        ch = input('erreur donner une chaine valide : ')   
    
    while ch!='':
        f.write(ch)
        ch = input('donner une autre chaine non vide')
        
    f.close()
    
def afficher(f):
    f = open("Original.txt",'r')
    fc = open('Copie.txt','w')
    i = 0
    ok = False
    while not ok:
        try:
            x = load
            
        except:
            ok = True
    
saisir()
afficher(f)