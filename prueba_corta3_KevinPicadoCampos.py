#Solicite al usuario elegir una opción de conversión:
#1. Dólares a Euros
#Euros a Dólares
#Solicite tres cantidades monetarias en la divisa fuente
# Realice las conversiones correspondientes. Determine y muestre:
#La cantidad mayor de las dos primeras en la divisa destino.
#La cantidad menor de las tres en la divisa destino.
#Un mensaje que indique si el promedio de cantidades está en categoría 
# "Presupuesto bajo" (0-100 unidades), "Presupuesto medio" (100-500 unidades) o "Presupuesto alto" (más de 500 unidades).
#Fórmulas
#• Dólares a Euros: E = D * 0.85
#• Euros a Dólares: D = E * 1.18

dolares1= 0
dolares2= 0
dolares3= 0
euros1= 0
euros2= 0
euros3= 0

def convertidor_de_dolares_a_euros(dolares1):
    dolares1 = float(input("Ingrese la cantidad que sea convertir a los euros:"))
    euros= dolares1 *0.85
    return euros
def convertidor_de_dolares_a_euros(dolares2):
    dolares2 = float(input("Ingrese la cantidad que sea convertir a los euros:"))
    euros= dolares2 *0.85
    return euros
def convertidor_de_dolares_a_euros(dolares3):
    dolares3 = float(input("Ingrese la cantidad que sea convertir a los euros:"))
    euros= dolares3 *0.85
    return euros
def convertidor_de_euros_a_dolares(euros1):
    euros1 = float(input("Ingrese la cantidad que sea convertir a los dolares:"))
    dolares= euros1 *1.18
    return dolares   
def convertidor_de_euros_a_dolares(euros2):
    euros2 = float(input("Ingrese la cantidad que sea convertir a los dolares:"))
    dolares= euros2 *1.18
    return dolares   
def convertidor_de_euros_a_dolares(euros3):
    euros3 = float(input("Ingrese la cantidad que sea convertir a los dolares:"))
    dolares= euros3 *1.18
    return dolares   

def main():
    opcion_a_escoger = int(input("ponga la opcion que desea convertir:\n1. dolares a euros \n2, euros a dolares: "))
    if opcion_a_escoger == 1:
        dolares1 = float(input("ingrese la cantidad en dolares a convertir en euros"))
        euros1 = convertidor_de_dolares_a_euros(dolares1)
        dolares2 = float(input("ingrese la cantidad en dolares a convertir en euros"))
        euros2 = convertidor_de_dolares_a_euros(dolares2)
        dolares3 = float(input("ingrese la cantidad en dolares a convertir en euros"))
        euros3 = convertidor_de_dolares_a_euros(dolares3)
        print(f"La cantidad en euros es: {euros1  + euros2 + euros3 }")
    elif opcion_a_escoger == 2:
        euros1 = float(input("ingrese la cantidad en euros a convertir en dolares"))
        dolares1 = convertidor_de_dolares_a_euros(euros1)
        euros2 = float(input("ingrese la cantidad en euros a convertir en dolares"))
        dolares2 = convertidor_de_dolares_a_euros(euros2)
        euros3 = float(input("ingrese la cantidad en euros a convertir en dolares"))
        dolares3 = convertidor_de_dolares_a_euros(euros3)
        print(f"La cantidad en euros es: {euros1  + euros2 + euros3 }")

    else:
        print("opcion no valida")

if __name__ == "_main__":
    main()

    def main():
        if dolares1 > dolares2:
            print(f"La cantidad mayor de las dos primeras en la divisa destino es: {dolares1} ")
        else:
            print(f"la cantidad mayor de las dos primeras en la divisa destino es: {dolares2} ")
            if dolares1 < dolares2 and dolares1 < dolares3:
                print(f"La cantidad menor de las tres en la divisa destino es: {dolares1}")
                if dolares2 < dolares1 and dolares2 < dolares3:
                  print(f"La cantidad menor de las tres en la divisa destino es: {dolares2}")
                else:
                    print(f"la cantidad menor de las tres en la divisa destino es: {dolares3}")
                
def promedio():
    promedio = (dolares1 + dolares2 + dolares3) /3 
    if promedio <= 100:
        print("Presupuesto bajo")

    elif promedio <=500:
        print("Presupuesto medio")
    else:
        print("Presupuesto alto")

def promedio():
    promedio = (euros1 + euros2 + euros3) /3 
    if promedio <= 100:
        print("Presupuesto bajo")

    elif promedio <=500:
        print("Presupuesto medio")
    else:
        print("Presupuesto alto")

                
