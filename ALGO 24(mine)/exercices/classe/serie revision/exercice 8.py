def remplir(ch,T,n)
ch = ch+' '
nb = -1
i = -1
while (ch != ''):
    ch1= ch[:ch.find(' ')]
    nb += 1
    ch = ch[ch.find(' '):]
    if palindrome(ch1):
        i += 1
        T[i]["mot"] = ch1
        T[i]["num"] = nb