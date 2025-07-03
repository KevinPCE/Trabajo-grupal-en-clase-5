def main():
    numeros_negativos = []
    numeros_positivos = []
    
    print("Ingrese 10 números enteros (pueden ser positivos o negativos):")
    
    for i in range(1, 11):
        while True:
            try:
                numero = int(input(f"Ingrese el número {i}: "))
                if numero < 0:
                    numeros_negativos.append(numero)
                elif numero > 0:
                    numeros_positivos.append(numero)
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
    
    # Calcular sumatoria de negativos
    sumatoria_negativos = sum(numeros_negativos)
    
    # Calcular promedio de positivos
    if len(numeros_positivos) > 0:
        promedio_positivos = sum(numeros_positivos) / len(numeros_positivos)
    else:
        promedio_positivos = 0
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"Sumatoria de números negativos: {sumatoria_negativos}")
    
    if len(numeros_positivos) > 0:
        print(f"Promedio de números positivos: {promedio_positivos:.2f}")
    else:
        print("No se ingresaron números positivos para calcular el promedio.")

if __name__ == "__main__":
    main()