ft = open('test1.txt','w')
n = int(input('nbr lignes : '))
while not (2<=n<=10):
    n = int(input('nbr lignes : '))
for i in range(n):
    ch = input('donner chaine n°'+str(i+1)+' : ')
    ft.write(ch+'\n')
ft.close()
ft = open('test1.txt','r')
res = ft.readline()
while res!='':
    print(res)
    res = ft.readline() 
print(res)
    
    
