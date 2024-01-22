ch = '1239'
def verif(ch):
    i = 0
    while (ch[i]<ch[i+1]) and (i<=len(ch)-2):
        i+=1
        print(i)

    j = 0
    while (ch[j]>ch[j+1]) and (j<=len(ch)-2):
        j+=1
        print(j)
    return i == len(ch)-1 or j == len(ch)-1 
verif(ch)