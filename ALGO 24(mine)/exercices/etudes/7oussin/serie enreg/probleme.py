from numpy import array


def saisir():
    global n
    n = int(input('donner n : '))
    while not (n <= 5000 and n > 1):
        n = int(input('donner n : '))


def valide(ch):
    ch1 = ""
    j = 0
    while ((ch[i].upper() in ["A", "F", "I", "P"]) and (ch1.find(ch[j].upper()) != -1)):
        j += 1
        ch1 += ch[j]


def remplir():
    global f
    f = open('SMS.dat', 'wb')
    for i in range(n):
        e = {}
        e["sms"] = input('sms : ')
        while not (valide(e["sms"])):
            e["sms"] = input('sms : ')
        e["tel"] = input("donner le numero de telephone : ")
        dump(e, f)
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
    f = open('SMS.dat', 'rb')
    for i in range(n):
        e = load(f)
        Foot["numero"] = e["tel"]
        Foot["classement"] = e["sms"]
        Foot["score"] = calcul_score(e["sms"])


def meilleur_score(t, n):
    maxi = t[0]
    for i in range(n):
        if t[i] > maxi:
            maxi = t[i]
    return maxi

# def dist(t,n,x):


def creer():
    global NT, n1
    n1 = 0
    maxi = meilleur_score(Foot, n)
    for i in range(n):
        if (Foot[i]["score"] == maxi) and dist(NT, n1, Foot[i]["numero"]):
            NT[i] == Foot[i]["numero"]
            n1 += 1


# pp
saisir()
remplir()
Foot = array([{}]*n)
former()
creer()
