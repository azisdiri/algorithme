# fonctions
def verif(ch):
    op = ch[0] in ['+', '-', '*', '/']
    i = 1
    nb = 0
    while (i < len(ch)) and (('1' <= ch[i] <= '9') or (ch[i] == ' ')):
        if ch[i] == ' ':
            nb += 1
        i += 1
    return op and (i == len(ch)) and nb == 1 and ch[len(ch)-1] != ' '


def exp(ch):
    pt1 = ch[1:ch.find(' ')]
    op = ch[0]
    pt2 = ch[ch.find(' ')+1:]
    a = int(pt1)
    b = int(pt2)
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    else:
        res = a/b
    return pt1+op+pt2+"="+str(res)

# procedures


def remplir():
    global f1, n
    f1 = open('operations.txt', 'w')
    n = 0
    rep = ''
    while rep.upper() != 'N':
        ch = input('donner une chaine : ')
        while not (verif(ch)):
            ch = input('erreur donner une chaine : ')
        f1.write(ch+"\n")
        n += 1
        rep = input('continuer O/N?')
        while not (rep.upper() in ['O', 'N']):
            rep = input('continuer O/N?')
    f1.close()


def evaluer():
    global f2
    f1 = open('operations.txt', 'r')
    f2 = open('calcul.txt', 'w')
    for i in range(n):
        ch = f1.readline()
        f2.write(exp(ch)+'\n')
    f1.close()
    f2.close()


def afficher():
    f2 = open('calcul.txt', 'r')
    ch = f2.readline()
    while ch != '':
        print(ch)
        ch = f2.readline()
    f2.close()


# pp
remplir()
evaluer()
afficher()
