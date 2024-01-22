ch = input('donner ch : ')
n = len(ch)
cle = n
ch1 = ''
for i in range(n):
    asc = ord(ch[i]) + cle
    print(asc)
    if ch[i] == ch[i].upper():
        if asc > 90:
            # asc = 65 + (asc - 91) % 26
            asc = (asc - 90) + 64
            print(asc)
    else:
        if asc > 122:
            # asc = 97 + (asc - 123) % 26
            asc = (asc - 122) + 96
            print(asc)
    ch1 += chr(asc)

print(ch1)
