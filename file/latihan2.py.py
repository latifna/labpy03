n = int(input(" Silahkan masukkan jumlah bilangan ="))
if n>0:
    i=1
    x=int(input(" Masukkan bilangan "+str(i)+"="))
    max=x;total=x
    for i in range(2,n+1):
        x=int(input(" Masukkan bilangan "+str(i)+"="))
        total+=x
        if max<x:
            max=x

    print(" Bilangan terbesar = ", max)