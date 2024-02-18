def anagramme(ch, ch1):
    ch = ch.upper()
    ch1 = ch1.upper()
    i = 0
    existe = True
    while (i < len(ch) and existe):
        j = 0
        while (j < len(ch1) and (ch[i] != ch1[j])):
            j += 1
        if j == len(ch1):
            existe = False
        else:
            ch1 = ch1[:ch1.find(ch[i])]+ch1[ch1.find(ch[i])+1:]
        i += 1
    return i == len(ch)

ch = input('donner chaine no1: ')
ch1 = input('donner chaine no2: ')
print(anagramme(ch, ch1))
