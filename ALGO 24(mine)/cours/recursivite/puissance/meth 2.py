def puiss(x,p):
    if p == 0 :
        return 1
    elif p>0:
            return (x*puiss(x,p-1))
    else:
            return (1/x)*(puiss(x,p+1))
##pp
x = int(input('donner x : '))
p = int(input('donner p : '))
print(puiss(x,p))
