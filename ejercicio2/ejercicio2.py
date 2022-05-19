a=int(input("dijite el valor de a:"))
b=int(input("dijite el valor de b:"))
if a<b :
    cant_num=0
    a=a+1
    while a<b:
        cant_num=cant_num+1
        a=a+1
    print("la cantidad de numeros del rango es" , cant_num)
else:
    print("a debe ser menor que b")