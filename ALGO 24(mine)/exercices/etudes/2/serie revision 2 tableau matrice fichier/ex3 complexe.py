from numpy import array
from math import sqrt


def saisir():
    global n
    n = int(input('donner n : '))
    while not (2 <= n <= 20):
        n = int(input('erreur donner n : '))


def remplir_t():
    for i in range(0, n):
        a = int(input('donner a : '))
        while a == 0:
            a = int(input('donner a : '))
        b = int(input('donner b : '))
        while b == 0:
            b = int(input('donner b : '))
        t[i] = str(a) + '+' + str(b) + 'i'


# pp
saisir()
t = array([str()]*n)
m = array([int()]*n)
remplir_t()
# remplir_m()
print(t)
