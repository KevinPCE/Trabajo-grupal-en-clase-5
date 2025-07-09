def main():
      numeros_negativo = []
      numeros_positivo = []
      print("Ingrese 10 números enteros pueden ser positivos o negativos pero deben de ser enteros:")
      for i in range(1, 11):
        while True:
            try:
                numero = int(input(f"Ingrese número {i}: "))
                if numero < 0:
                    numeros_negativo.append(numero)
                elif numero > 0:
                    numeros_positivo.append(numero)
                break
            except ValueError:
                print(" Por favor ingrese un número entero válido.")   
# Calcular sumatoria negativs
      sumatoria_negativos = sum(numeros_negativo)
# Calular promedi positivos
      if len(numeros_positivo) > 0:
        promedio_positivo = sum(numeros_positivo) / len(numeros_positivo)
      else:
        promedio_positivo = 0    
# resultados
      print("\nResultados:")
      print(f"Sumatoria de números negativos: {sumatoria_negativos}")
    
      if len(numeros_positivo) > 0:
        print(f"Promedio de números positivos: {promedio_positivo:.2f}")
      else:
        print("No se ingresaron números positivos no se puede calcular el promedio.")

if __name__ == "__main__":
    main()