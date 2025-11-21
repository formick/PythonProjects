from itertools import count
from multiprocessing.util import sub_debug

pole = [5,2,9,1,7,3,10,6,4]
pole2 = [3,5,4,7,5,3,4,5,10]
pole_vysledne = []
for i in range(len(pole)):
    pole_vysledne.append(pole[i] + pole2[i])

print(pole_vysledne)

pole = [5,2,9,1,7,3,10,6,4]
pole2 = [3,5,4,7,5,3,4,5,10]
pole_vysledne = []

for i in range(len(pole)):

    pole_vysledne.append(pole[i] + pole2[-i-1])

print(pole_vysledne)

#najdete druhe nejvetsi prvek v poli
#if pole[i]>max
    #max = -100000  druhy = -100000
    #= float('-inf')

if len(pole) >= 2:
    if pole[0] > pole[1]:
        max = pole[1]
        druhy = pole[0]
for i in range(len(pole)):
    if pole[i] > max:
        druhy = max
        max = pole[i]
    elif pole[i] > druhy:
        druhy = pole[i]

print(druhy)

#****************************************************
pole = [5,2,9,1,7,3,10,6,4]
je = True
for i in range(len(pole)-1):
    if pole[i] > pole[i+1]:
        je = False
        break

if je:
    print("serazene")
else: print("neni serazene")

#*************************************************
pole = [5,2,9,1,7,3,10,6,4]
sude = 0
liche = 0
for i in range(len(pole)):
    if  pole[i] % 2 == 0:
        sude +=1
    else:
     liche +=1

print(sude)
print(liche)