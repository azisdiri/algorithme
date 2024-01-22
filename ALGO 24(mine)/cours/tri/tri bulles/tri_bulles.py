def saisir():
	global n
	n=int(input("saiair taille:"))
	while not(n>0):
		n=int(input("saiair taille:"))
def remplir(t,n):
	for i in range(n):
		t[i]=randint(1,99)
def afficher(t,n):
	for i in range(n):
		print(t[i],end="|")
	print()
def tri_bulles(t,n):
	ok=True
	while (ok)and n!=1:
		permut=False
		for i in range(n-1):
			if t[i]>t[i+1]:
				t[i],t[i+1]=t[i+1],t[i]
				permut=True
		n-=1
#--------pp-----------
from random import randint
from numpy import array
saisir()
t=array([int()]*n)
remplir(t,n)
afficher(t,n)
tri_bulles(t,n)
afficher(t,n)