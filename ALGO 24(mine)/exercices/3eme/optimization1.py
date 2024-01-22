def saisir():
    global ep
    ep = float(input('inserer la valeur de epsilon: '))
    while not(ep>0):
        ep = float(input('inserer une valeur strictement superiere a 0: '))

def calculx(ep):
    x = 0
    vmax = 0
    xmax = 0
    while not(x>5):
        x += ep
        v = 100*x-40*x*x+4*x*x*x
        print("x = ",'%.4f'%x,"v = ",'%.4f'%v)
        if v>vmax:
            vmax = v
            xmax = x
    return ("%.4f" % xmax)
##pp
saisir()
print('la valeur optimale de x est : ',calculx(ep))
        