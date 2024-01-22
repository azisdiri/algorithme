def saisir():
    global n
    n = int(input('donner n : '))
    while not(n>=13):
        n = int(input('err donner n : '))
def div13(n):
    ch = str(n)
    signe = -1
    s = 0
    while len(ch)>3:
        ch1 = ch[len(ch)-3:len(ch)]
        s = s+(signe*int(ch1))
        ch = ch[0:len(ch)-2]
        s = s+ signe*int(ch)
    return abs(s)%13 == 0 
saisir()
print(div13(n))