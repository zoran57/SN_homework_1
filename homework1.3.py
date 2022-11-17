#računske operacije
"""
brojA= int(input("unesite brojA:"))
brojB= int(input("unesite brojB:"))

print( brojA + brojB )
"""
"""
brojA= int(input("unesite brojA:"))
brojB= int(input("unesite brojB:"))

operacijaZ = input("unesite +:")
if operacijaZ == "+":
    print(brojA + brojB)
else:
    operacijaM = input("unesite -:")
if operacijaM == "-":
    print(brojA - brojB)
else:
    operacijaMN = input("unesite *:")
if operacijaMN == "*":
     print(brojA * brojB)
else:
    operacijaD= input("unesite /:")

if operacijaD == "/":
    print(brojA / brojB)
"""

brojA= int(input("unesite brojA:"))
brojB= int(input("unesite brojB:"))
operacijaZ = input("unesite +, -,* ili /:")

if operacijaZ == "+":
    print(brojA + brojB)
elif operacijaZ == "-":
    print(brojA - brojB)
elif operacijaZ == "*":
    print(brojA * brojB)
elif operacijaZ == "/":
    print(brojA / brojB)
