def remplir():
    global e1, e2
    e1 = {}
    e2 = {}
    e1["Re"] = int(input("donner a : "))
    e1["Im"] = int(input("donner b : "))
    e2["Re"] = int(input("donner c : "))
    e2["Im"] = int(input("donner d : "))


# pp
remplir()
a = e1["Re"]
b = e1["Im"]
c = e2["Re"]
d = e2["Im"]
print("somme = "+str(a+c)+"+"+str(b+d)+"*i")
print("produit = "+str(a*c-b*d)+"+"+str(a*d+b*c)+"*i")
print("division = "+str((a*c+b*d)/(c*c+d*d))+"+"+str((b*c-a*d)/(c*c+d*d))+"*i")
