vstup = input("Zadej cislo: ")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup =" + vstup)

#if cislo < 10:
    #print("cislo je mensi nez 10")
#if 20 > cislo > 10:
    #print("cislo je vetsi nez 10 a mensi nez 20")
#if cislo > 20:
    #print("cislo je vetsi nez 20")


if cislo > 10:
    print("cislo je vetsi nez 10")
if cislo % 2 == 0:
    print("sude")
else:
    print("liche")
if 20 > cislo > 10:   #if cislo > 10 and cislo < 20:
    print("cislo je vetsi nez 10, ale mensi nez 20")

#privit, lalalala, cau hello lalalala




