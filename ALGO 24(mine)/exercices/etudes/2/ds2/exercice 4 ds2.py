def verif(a,b):
    while a!=b:
        if (a>b):
            a=a-b
        else:
            b=b-a
    return a==1


def premier(x):
    i=2
    while(i<=x//2)and(x%i!=0):
        i+=1
    return i==x//2+1


def remplir():
    global t
    t=array([0]*3)
    ok=False
    while not ok:
        p=randint(30,90)
        while not (premier(p)):
            p=randint(30,90)
        q=p+1
        while not(premier(q)):
            q+=1
        t[0]=int(input("t[0]:"))
        if (verif(t[0],(p-1)*(q-1))):
            ok=True   
    t[1]=p*q
    d=1
    while((t[0]*d)%((p-1)*(q-1)))!=1:
        d+=1
    t[2]=d-1
        
def puiss(x):
    for i in range(1,p+1):
        x=x*i
    return x


def rsa(chn):
    e=t[0]
    n=t[1]
    d=t[2]
    ch=""
    for i in range(len(chn)):
        ch+=ord(ch[i])
    while (len(ch)%(len(str(n))-1))!=0:
        ch="0"+ch
    res=""
    while ch!="":
        ch1=ch[:len(str(n))]
        ch=ch[len(str(n)):]
        while len(str(puiss(int(ch1),e)))%n!=(len(str(n))-1):
            ch1=str(puiss(int(ch1),e)%n)
        res+=ch1
    res1=""
    while res!="":
        res1+=chr(res[:3])
        res=res[3:]
    return res1

        
#pp
from random import randint
from numpy import array
remplir()
print(t)