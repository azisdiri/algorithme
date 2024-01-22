from numpy import array
t = array([str]*4)
ch = 'programmer est un art'
ch = ch + '  '
i = 0
while ch!=' ':
    t[i] = ch[:ch.find(' ')]
    ch = ch[ch.find(' ')+1:]
    i += 1
print(i)
print(t)