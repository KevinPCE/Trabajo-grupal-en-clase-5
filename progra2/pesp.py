#estado de peso de la persona

def main():
    peso = float(input("Ingrese su peso en kg: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    
    imc = peso / (estatura ** 2)
    
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
    
    if imc < 18.5:
        print("Estado: Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Estado: Peso normal")
    elif 25 <= imc < 29.9:
        print("Estado: Sobrepeso")
    elif 30 <= imc < 34.9:
        print("Estado: Obesidad grado I")
    elif 35 <= imc < 39.9:
        print("Estado: Obesidad grado II")
    else:
        print("Estado: Obesidad Extrema")


if __name__ == "__main__":
     main()
   