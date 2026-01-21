def matriz(filas, columnas, nombre):
    matriz = []
    print(f"\nIngrese los elementos de la matriz {nombre} ({filas} filas, {columnas} columnas):") 
    for i in range(filas): 
        while True:

           try:
            # Leer fila y convertir a lista de números
            print(f"Ingrese los elementos de la fila {i + 1} ")
            # fila = input(f"Fila {i+1}): ").strip().split()
  
            filas = input(f"Fila {i+1}): ").strip().split()

            if len(filas) != columnas:
                    print(f"Vamos a la siguiente fila {columnas} elementos")
                    
                
            fila_numeros = [float(elemento) for elemento in filas]
            matriz.append(fila_numeros)
            break
           except ValueError:
                print("Error: ingrese solo números válidos")
    
    return matriz

def multiplicar_las_matrices(matriz_a, matriz_b):
    """
    Función para multiplicar dos matrices
    """
    if not matriz_a or not matriz_b:
        raise ValueError("Las matrices no pueden estar vacías")
    if len(matriz_a[0]) != len(matriz_b):
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")
    filas_a = len(matriz_a)
    columnas_b = len(matriz_b[0])

def imprimir_matriz(matriz, nombre):
    print(f"\n{nombre}:")
    for fila in matriz:
        # Formatear cada número con 2 decimales y alinear
        fila_formateada = [f"{num:10.2f}" for num in fila]
        print(" ".join(fila_formateada))

def obtener_dimension(mensaje):
    """
    Función para obtener una dimensión válida desde la entrada
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Error: la dimensión debe ser un número positivo")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número entero válido")
def main():
    print("Bienvenido al programa de multiplicación de matrices")
    
    # Obtener dimensiones de las matrices
    filas_a = obtener_dimension("Ingrese el número de filas de la matriz A: ")
    columnas_a = obtener_dimension("Ingrese el número de columnas de la matriz A: ")
    filas_b = obtener_dimension("Ingrese el número de filas de la matriz B: ")
    columnas_b = obtener_dimension("Ingrese el número de columnas de la matriz B: ")

    # Leer las matrices
    matriz_a = matriz(filas_a, columnas_a, "A")
    matriz_b = matriz(filas_b, columnas_b, "B")
    resultado = [[0] * columnas_b for _ in range(filas_a)]  # Inicializar matriz resultado
# Realizar la multiplicación
    for i in range(filas_a):
     for j in range(columnas_b):
         for k in range(columnas_a):
            resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
            resultado[i][j] = round(resultado[i][j], 2)
    return filas_a, columnas_b, resultado

        

    # Imprimir resultados
    imprimir_matriz(matriz_a, "Matriz A")
    imprimir_matriz(matriz_b, "Matriz B")
    imprimir_matriz(resultado, "Resultado (A * B)")

if __name__ == "__main__":
    main()