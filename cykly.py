# for i in range(0,11,2):
#     print(i)
#     print("ahoj")
#      i nalezi 0,1,2...n-1
#     i nalezi <0;n)
#     reange a,n,s i nalezi <a;n), krok = s
# for i in range(0,11):
#     if i%2==0:
#         print(i)
#
# for i in range(5):
#     for j in range(5):
#         print(str(i) + ", " + str(j))






for i in range(10):
    print(i)
    if i > 5:
        break #continue
    print("ahoj")




a = 0
while True:
    x = input("napis cislo: ")
    try:
        a = int(x)
        break
    except:
        pass
print(a)