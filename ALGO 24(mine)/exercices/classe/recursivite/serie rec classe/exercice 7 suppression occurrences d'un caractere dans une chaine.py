'''
def supp(c,ch):
    p = ch.find(c)
    while not (p==-1):
        ch = ch[:p]+ch[p+1:]
        p = ch.find(c)
    return ch
'''
def supp(ch,c):
    p = ch.find(c)
    if p == -1:
        return ch
    else:
        return supp(ch[:p]+ch[p+1:],c)

#pp
ch = input('ch:')
c = input('c:')
print(supp(ch,c))
