from numpy import array


def ajouter():
    with open('operation.txt', 'a') as f1:
        ch = input('donner une chaine : ')
        # ken mana3mlch '\n' mllawl twali chaine jdida les9a fli 9balha
        f1.write('\n' + ch + '\n')


def supprimer():
    global t
    t = array([str()]*20)
    ts1()
    ts2()


def ts1():
    with open('operation.txt', 'r') as f1:
        global n
        n = 0
        ch = f1.readline()
        while ch != '':
            t[n] = ch
            n += 1
            ch = f1.readline()


def ts2():
    with open('operation.txt', 'w') as f1:
        p = int(input('donner une position a supprimer [0..'+str(n-1)+']'))
        for i in range(n):
            if (i != p):
                f1.write(t[i]+'\n')


def ts2_1():
    with open('operation.txt', 'w') as f1:
        p = int(input('donner une position a modifier [0..'+str(n-1)+']'))
        for i in range(n):
            if (i != p):
                f1.write(t[i]+'\n')
            else:
                ch = input('modification : ')
                f1.write(ch + '\n')


def afficher_numerote():
    pass


def modifier():
    global t
    t = array([str()]*20)
    ts1()
    ts2_1()


# pp
print('1_ajout ligne')
print('2_supprimer ligne')
print('3_afficher lignes numerotes')
print('4_modifier ligne')
print('5_quitter')
choix = int(input('choisissez un des catres procedures : '))
while not (1 <= choix <= 5):
    choix = int(input('choisissez un des catres procedures : '))
match choix:
    case 1:
        ajouter()
    case 2:
        supprimer()
    case 3:
        afficher_numerote()
    case 4:
        modifier()
    case _:
        print('quitter')
