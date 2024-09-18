import random
while True:
 age = input("Zadejte váš věk: ")
 if age.isdigit():
    print("Děkuji")
    break
 else:
    print("Zadej jen celočíselnou hodnotu.")# ukol cislo 4,9 a bonus

randomnumber= random.randint(1, 10)
print(randomnumber) #ukol 10

name = ("tobias")
name2 = ("rameš")
print(name)
print(name2)# ukoly cislo 1,2,3

print (len(name))
print (len(name2))# ukol 5

x = 6
for i in range(5):  
    x += 3
print(x)# ukol cislo 6,7,8