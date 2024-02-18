from pickle import *
f1 = open("Codes_Braille.dat", 'wb')
e = {}
e["lettre"] = "A"
e["codage"] = "*-----"
dump(e, f1)
e = {}
e["lettre"] = "B"
e["codage"] = "*-*---"
dump(e, f1)
e = {}
e["lettre"] = "C"
e["codage"] = "**----"
dump(e, f1)
e = {}
e["lettre"] = "D"
e["codage"] = "**-*--"
dump(e, f1)
e = {}
e["lettre"] = "E"
e["codage"] = "*--*--"
dump(e, f1)
e = {}
e["lettre"] = "F"
e["codage"] = "***---"
dump(e, f1)
e = {}
e["lettre"] = "G"
e["codage"] = "****--"
dump(e, f1)
e = {}
e["lettre"] = "H"
e["codage"] = "*-**--"
dump(e, f1)
e = {}
e["lettre"] = "I"
e["codage"] = "-**---"
dump(e, f1)
e = {}
e["lettre"] = "J"
e["codage"] = "-***--"
dump(e, f1)
e = {}
e["lettre"] = "K"
e["codage"] = "**-*-*-"
dump(e, f1)
e = {}
e["lettre"] = "L"
e["codage"] = "*-*-*-"
dump(e, f1)
e = {}
e["lettre"] = "M"
e["codage"] = "**-**-"
dump(e, f1)
e = {}
e["lettre"] = "N"
e["codage"] = "**--*-"
dump(e, f1)
e = {}
e["lettre"] = "O"
e["codage"] = "*--**-"
dump(e, f1)
e = {}
e["lettre"] = "P"
e["codage"] = "***-*-"
dump(e,f1)
e = {}
e["lettre"] = "Q"
e["codage"] = "****-*"
dump(e,f1)
e = {}
e["lettre"] = "R"
e["codage"] = "*-***-"
dump(e,f1)
e = {}
e["lettre"] = "S"
e["codage"] = "-**-*-"
dump(e,f1)
e = {}
e["lettre"] = "T"
e["codage"] = "-****-"
dump(e,f1)
e = {}
e["lettre"] = "U"
e["codage"] = "*-*-**"
dump(e,f1)
e = {}
e["lettre"] = "V"
e["codage"] = "*-*-*-*"
dump(e,f1)
e = {}
e["lettre"] = "W"
e["codage"] = "-***-*"
dump(e,f1)
e = {}
e["lettre"] = "X"
e["codage"] = "**--**"
dump(e,f1)
e = {}
e["lettre"] = "Y"
e["codage"] = "**-***"
dump(e,f1)
e = {}
e["lettre"] = "Z"
e["codage"] = "*--***"
dump(e,f1)
e = {}


f1.close()
