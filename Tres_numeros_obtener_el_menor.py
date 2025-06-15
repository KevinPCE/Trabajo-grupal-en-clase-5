cantidad=int(input("ingrese la cantidad de valores"))
minimo=255
maximo=-255
for i in range(cantidad):
    numero=int(input("ingrese el numero"))
    if numero<minimo and numero>maximo:
        minimo=numero
print("El numero menor es:",minimo)


   