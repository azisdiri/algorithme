s = int(input('seconds : '))
h = s//3600
s1 = s - 3600*h
m = s1//60
s2 = s1 - 60*m
if s2>=60:
    s2 -= 60
    m += 1
if m >= 60:
    m -= 60
    h += 1
print(h,'hrs')
print(m,"mn")
print(s2,"sec")