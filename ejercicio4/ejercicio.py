
#input

a=int(input("escribe el valor de a:"))
b=int(input("escribe el valor de b:"))
#processing

if 1<a:
    cant_num=0
    a=a+1
    while(a<=b):
        r=a%5
        if r ==0:
            cant_num=cant_num+1
        a=a+1
    print("la cantidad de numeros es" , cant_num)
else:
    print(" a debe ser mallor a 1")
