# Función que calcula la suma del 0 al 100
def calcular_suma():
    suma = 0
    for i in range(101):  # Incluye el 100
        suma += i
    return suma

# Función principal
def main():
    resultado = calcular_suma()
    print(f"La suma de los números del 0 al 100 es: {resultado}")

# Llamada a main
if __name__ == "__main__":
    main()

