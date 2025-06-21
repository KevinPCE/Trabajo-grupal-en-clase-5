
#Desarrollar un programa en Python que determine si un año es bisiesto.

#Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

#Restricciones

#1.Se pueden ingresar solo números positivos.
#2.Los números a ingresar deben estar entre 1,500 y 2,030.
#3.Debe usar funciones para separar el código de forma apropiada y con la buena práctica vista en clase.
#Para ello realice el algoritmo, pseudocodigo y programa en Python.

año = int(input("Ingrese un año entre 1500 y 2030: "))
while año < 1500 or año > 2030:
    print("El año debe estar entre 1500 y 2030. Intente de nuevo.")
    año = int(input("Ingrese un año entre 1500 y 2030: "))
def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:   
        return False
print(f"El año {año} {'es' if es_bisiesto(año) else 'no es'} bisiesto.")
# Fin del programa