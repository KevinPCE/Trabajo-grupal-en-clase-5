#1. Escriba un programa usando Python 3 que permita al usuario ingresar 10 números enteros, que pueden ser positivos o negativos.
#Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#Notas:
#No olvidar que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error 
# si no se ingresaron números positivos o letras.

def main():
    suma_negativos = 0
    contador_positivos = 0
    numeros_positivos = []
    
    #print("Ingrese 10 números enteros, pueden ser positivos o negativos")
    
    for i in range(1, 11):
        while True:
            try:
                numero = int(input(f"Ingrese el número {i}: "))
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
        
        if numero < 0:
            suma_negativos += numero
        else:
            numeros_positivos.append(numero)
            contador_positivos += 1
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"Suma de números negativos: {suma_negativos}")
    
    if contador_positivos > 0:
        promedio_positivos = sum(numeros_positivos) / contador_positivos
        print(f"Promedio de números positivos: {promedio_positivos:.2f}")
    else:
        print("No se ingresaron números positivos para calcular el promedio.")

if __name__ == "__main__":
    main()