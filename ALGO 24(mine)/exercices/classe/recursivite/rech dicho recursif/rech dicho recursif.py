from numpy import array

def remplir():
    global t
    for i in range(n):
        t[i] = int(input("un entier bllehi: "))
        
def dicho(t, n, x, d, f):
    if f >= d:
        m = (d + f) // 2
        if t[m] == x:
            return True
        elif t[m] > x:
            return dicho(t, n, x, d, m - 1)
        else:
            return dicho(t, n, x, m + 1, f)
    else:
        return False



##
n = int(input("donner n : "))
t = array([int()]*n)
remplir()
x = int(input('donner x: '))
print(dicho(t,n,x,0,n-1))