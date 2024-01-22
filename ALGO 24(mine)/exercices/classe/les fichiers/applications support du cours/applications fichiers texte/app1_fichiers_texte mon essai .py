def creation():
    with open ('original.txt','w') as f1:
        rep = ''
        while not (rep.upper() == 'N'):
            ch = input('donner une chaine  : ')
            f1.write(ch+'\n')
            rep = input('cont?')
            while not(rep.upper() in ['O','N']):
                rep = input('cont?')

def copier():
    with open ('original.txt','r') as f1:
        with open('copie.txt','w') as f2:
            ch = f1.readline()
            n = -1
            while ch!='':
                n = n+1
                print(n)
                f2.write(str(n)+ch+'\n')
                ch = f1.readline()    
#pp
creation()
copier()