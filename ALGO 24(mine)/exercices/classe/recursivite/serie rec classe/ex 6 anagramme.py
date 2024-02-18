def anag(ch1,ch2):
    if ch1=="" and ch2=="":
        return True
    else:
        p = ch2.find(ch1[0])
        if p != 1:
            return anag(ch1[1:],ch2[:p]+ch2[p+1:])
        else:
            return False
        
##pp
ch1 = input("ch1: ")
ch2 = input("ch2: ")
print(anag(ch1,ch2))