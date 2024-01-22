from numpy import array

def palindrome(mot):
    i = 0
    while i <= len(mot) // 2 - 1 and mot[i].upper() == mot[len(mot) - i - 1].upper():
        i += 1
    return i == len(mot) // 2

def saisir():
    global ch
    ch = input('donner ch : ')
    while ch == '':
        ch = input('erreur donner ch : ')

def former():
    global T
    T = []
    ch_copy = ch + ' '  # Create a copy to avoid modifying the global 'ch'
    i = -1
    nb = -1
    while ch_copy != '':
        ch1 = ch_copy[:ch_copy.find(' ')]
        nb += 1
        ch_copy = ch_copy[ch_copy.find(' ') + 1:]
        if palindrome(ch1):
            i += 1
            T.append({"mot": ch1, "Num": nb})

# Initialize global variables
ch = ""
T = []

saisir()
former()
print(T)
