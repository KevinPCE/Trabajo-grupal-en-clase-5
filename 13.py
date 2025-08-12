def es_valido(numero):
    for digito in numero:
        if digito not in "0123456789":
            return False
    return True

def agregar_si(condicion, cadena, numero):
    if condicion:
        return cadena + numero + ", "
    return cadena

cadena_digitos_mult5 = ""
cadena_multiplos_5 = ""
cadena_contiene_100 = ""
cadena_contiene_1 = ""

while True:
    numero = input("Número: ")

    if len(numero) > 0 and numero[0] == '-':
        break
    if not es_valido(numero):
        continue

    num = int(numero)

    if num % 20 == 0 or num < 0:
        break

    # Condiciones y agregados
    cadena_digitos_mult5 = agregar_si(len(numero) % 5 == 0, cadena_digitos_mult5, numero)
    cadena_multiplos_5 = agregar_si(num % 5 == 0, cadena_multiplos_5, numero)
    cadena_contiene_100 = agregar_si("100" in numero, cadena_contiene_100, numero)
    cadena_contiene_1 = agregar_si("1" in numero, cadena_contiene_1, numero)

# Agregar *UH* al final
cadena_digitos_mult5 += "*UH*"
cadena_multiplos_5 += "*UH*"
cadena_contiene_100 += "*UH*"
cadena_contiene_1 += "*UH*"

# Mostrar resultados
print("\nNúmeros cuya cantidad de dígitos es múltiplo de 5:", cadena_digitos_mult5)
print("Números que son múltiplos de 5:", cadena_multiplos_5)
print("Números que contienen el 100:", cadena_contiene_100)
print("Números que contienen el 1:", cadena_contiene_1)

