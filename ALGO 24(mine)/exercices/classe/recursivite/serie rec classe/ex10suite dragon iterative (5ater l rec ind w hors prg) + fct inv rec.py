def inverse(ch):
    ch1 = ''
    if ch=='':
        return ''
    else:
        if ch[len(ch)-1] == "D":
            return "G"+inverse(ch[:len(ch)-1])
        else:
            return "D"+inverse(ch[:len(ch)-1])
        
            
def dragon(n):
    u0 = "D"
    for i in range (1,n+1):
        u0=u0+"D"+inverse(u0)
    return u0
    
n = int(input('n: '))
print(dragon(n))
