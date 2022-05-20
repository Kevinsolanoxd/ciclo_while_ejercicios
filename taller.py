c=int(input("ingrese la cantidad que va a poner: "))

n=0
D=c*2


while c<D:
    c=c+0.05*c
    n=n+1
else:
    print("en %s meses se va a duplicar su invercion" % (n))