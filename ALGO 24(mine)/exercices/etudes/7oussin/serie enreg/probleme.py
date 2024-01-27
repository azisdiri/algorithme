from numpy import array
def saisir():
    global n
    n = int(input('donner n : '))
    while not (n<=5000 and n>1):
        n = int(input('donner n : '))
   
todo def valide():
    
   
def remplir():
    global f
    f = open('SMS.dat','wb')
    for i in range(n):
        e = {}
        e["sms"] = input('sms : ')
        while not (valide(e["sms"])):
            e["sms"] = input('sms : ')
        e["tel"] = input("donner le numero de telephone : ")
        dump(e,f)
    f.close()
    
def calcul_score(ch):
         ch = ch.upper()
         ch1 = "IFAP"
         s = 4
         for i in range(len(ch)):
             if ch[i] != ch1[i]:
                 s -= 1
        return s*25

def former():
    global Foot
    f = open('SMS.dat','rb')
    for i in range(n):
        e = load(f)
        Foot["numero"] = e["tel"]
        Foot["classement"] = e["sms"]
        Foot["score"] = calcul_score(e["sms"])
        

      
      
      
#pp
saisir()
remplir()
Foot = array([{}]*n)
former()
