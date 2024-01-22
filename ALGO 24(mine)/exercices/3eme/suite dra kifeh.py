from math import sqrt
eps = 0.00001
def pi_euler(eps):
    s1 = 1
    s2 = 1/4
    i = 3
    while not (abs(sqrt(s1*6) - sqrt(s2*6))<= eps):
        s1 = s2
        s2 = s2 + 1/ i*i
    return sqrt(s2*6)

print(pi_euler(eps))