from math import sqrt
def saisir():
    global eps
    eps = float(input('inserer la valeur de epssilon: '))
    while not(eps>0):
        eps = float(input('inserer une valeur strictement superiere a 0: '))
def Pi_Euler(eps):
    s2 = 1+1/4
    s1 = 1
    i = 3
    while not(abs(sqrt(6*s1)-sqrt(6*s2))<=eps):
        s1 = s2
        s2 = s1+1/(i*i)
        i+=1
    return sqrt(6*s2)

##pp
saisir()
print('la valeur optimale de pi est : ',Pi_Euler(eps))
        
