def generar_matriz(n, m): 
#Genera una matriz de n filas y m columnas con las siguientes condiciones:"
#Desarrollar un programa en Python que genere una matriz de n filas y m columnas con la
#siguiente estructura (8x9)
    matriz = []
    for i in range(n):
         fila = []
         if i ==   0:
            fila.append(1)
            for j in range(1, m):
                fila.append(0)
         elif i == 1:
            for j in range(m):
                fila.append(1)
         else:
            for j in range(m):
                fila.append((i) ** j)
         matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:  
        # Imprimir cada fila de la matriz
        # Convertir cada elemento a cadena y unirlos con un espacio
        print(' '.join(map(str, fila))) 

def main():
    while True: 
        try: 
            n = int(input("Ingrese número de filas n: "))
            m = int(input("Ingrese número de columnas m: "))
            if n > 0 and m > 0:
                break
            else:
                print("ingrese números positivos.")   
        except ValueError: 
            print("ingrese números enteros válidos.")
    
    matriz = generar_matriz(n, m)   
    imprimir_matriz(matriz)  

if __name__ == "__main__":
    main() 


