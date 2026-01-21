def main():

    numeros = []
    #numeros=int(input("Ingrese un número entero"))
    print("El número que ingresó es:", numeros)

    for i in range(1, 11):
        while True:
            try:
                numero = int(input(f"Ingrese número {i}: "))
                numeros.append(numero)
                break
            except ValueError:
                print(" Por favor ingrese un número entero válido.")

    print("Los números ingresados son:", numeros)

    #Promedio de los números ingresados

    if len(numeros) > 0:
        promedio_positivo = sum(numeros) / len(numeros)
    else:
        promedio_positivo = 0
    print(f"Promedio de números ingresados: {promedio_positivo:.2f}")

    #Número mayor y menor
    numero_mayor = max(numeros)
    numero_menor = min(numeros)
    print(f"Número mayor ingresado: {numero_mayor}")
    print(f"Número menor ingresado: {numero_menor}")

    #suma de los números ingresados
    suma_numeros = sum(numeros)
    print(f"Suma de los números ingresados: {suma_numeros}")

if __name__ == "__main__":
    main()