def creation():
    global f1
    f1=open("CodeBraille.dat","wb")
    for i in range(26):
        e={}
        e["lettre"]=chr(i+65)
        e["codage"]=input(e["lettre"]+"=>"+"")
        dump(e,f1)

def equivalent(ch):
    f1=open("CodeBraille.dat","rb")
    c=""
    ok=False
    eof=False 
    while (not (eof and ok)):
        try:
            e=load(f1)
            if(e["codage"]==ch):
                c=e["lettre"]
                ok=True
        except:
            eof=True
    f1.close()
    return c

    

def afficher():
    f2 = open("Braille.txt","r")
    res=""
    ch = f2.readline()
    while ch!='':
        mot=""
        for i in range(0,len(ch),6):
            mot+=equivalent(ch[i:i+6])
        ch = f2.readline()
        res+=mot+" "
    f2.close()
    print(res[:len(res)-1])

#PP
from pickle import *
#creation()
afficher()