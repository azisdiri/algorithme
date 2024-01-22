def saisir():
    global eps
    eps = float(input('donner epsilon : '))
    while not(eps>0):
        eps = float(input('erreur donner epsilon : '))


def Pi_wallis(eps):
    s2 = 4/3
    i = 2
    s1 = 1
    while not(abs(s1 - s2)<=eps):
        s1 = s2
        s2 = s1 * (2*i/(2*i-1))*(2*i/(2*i+1))
        i += 2
    return 2*s2

saisir()
print('la valeur approchee de pi est :',Pi_wallis(eps))