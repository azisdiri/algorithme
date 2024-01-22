from math import *
def pi_euler(eps):
    sp = 1
    s = 1 + 1/4
    i = 3
    while not (abs(sqrt(sp*6) - sqrt(s*6))<= eps):
        sp = s
        s = s + 1/ (i*i)
        i += 1
    return sqrt(s*6)

print('pi euler = :',pi_euler(0.00000000000000000000000001))
print('pi',pi)