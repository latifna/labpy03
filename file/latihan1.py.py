import random
print(40*"=")
print("Bilangan random yang lebih kecil dari 0,5")
print(40*"=")
bil = int( input("Masukkan nilai n :"))
i = 0
for i in range(bil):
    i += 1
    angkaDec = random.uniform(0, 0.5)
    print(" Data ke ", i, " = " , angkaDec)