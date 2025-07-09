n=int(input("Ingrese un número entero positivo: "))
def divisores(numero):
      divisores_lista = []
      for i in range(1, numero + 1):
        if numero % i == 0:
            divisores_lista.append(i)
      return divisores_lista

#uso:
numero = n
print(f"Los divisores de {numero} son: {divisores(numero)}")