vstup = input("zadej cislo: ")
try:
    cislo = int(vstup)
except:
    cislo = 0
    print("vstup = " + vstup)

if cislo > 5:
        print("cislo")
        print(cislo)
        print("vetsi")
        print("je")
        print("vetsi nez 5")
        if cislo > 10:
            print("nevim, neco")

else:
    print("neni vetsi nez 5")
if cislo < 7:
    print("cislo je mensi nez 7")
print("konec")

a = input("zadej A")
b = input("zadej B")
c = input("zadej C")

d = b**2 - 4*a*c
if d > 0:
        print("nula reseni v R.")
elif d == 0:
        print("jedno reseni v R.")
else:
        print("dve reseni v R.")
