print("ahoj")

odpoved = input("tohle se napise do radky: ")

print(odpoved)
print(type(odpoved))

#odpoved_jako_cislo = int(odpoved)
# odpoved_jako_cislo = float(odpoved)
try:
    odpoved_jako_cislo = int(odpoved)
except:
    print("ty jsi ale peknej *****, ze neumis zadat cislo, nastavuju na 0")
    odpoved_jako_cislo = 0

print("ahoj " + "vole")

print(22 + odpoved_jako_cislo)

