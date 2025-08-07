#Escribir un programa que permita al usuario ingresar números que serán leídos hasta que ingrese uno que sea múltiplo de 20 o menor que 0, se formarán 4, en los cuales se concatenaran los números ingresados, según el siguiente criterio: 1 cadenas en las que concatenarán todos lo números que el usuario ingrese cuya cantidad de dígitos sea un múltiplo de 5, en la segunda cadena se concatenarán todos lo números que el usuario ingrese que sean múltiplos de 5, en el otro se concatenarán todos los números que contengan el digito 100, en el otro se concatenarán todos los números que contengan el digito 1. Si un número cumple todas las condiciones debe concatenarse en todas las cadenas, en cada cadena al final de todos los números concatenados debe de colocarse la frese "UH", Al finalizar, mostrar en pantalla todas las cadenas

# Inicializamos las 4 cadenas
cadena_mult5_digitos = ""
cadena_mult5_numeros = ""
cadena_contiene_100 = ""
cadena_contiene_1 = ""

while True:
    # Leer número del usuario
    numero = input("Ingrese un número (el programa terminará si es múltiplo de 20 o menor que 0): ")
    
    # Verificar si es un número válido
    try:
        num = int(numero)
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue
    
    # Condición de terminación
    if num % 20 == 0 or num < 0:
        break
    
    # Convertir el número a string para verificar condiciones
    num_str = str(num)
    
    # Verificar condiciones y concatenar en las cadenas correspondientes
    
    # 1. Cantidad de dígitos es múltiplo de 5
    if len(num_str) % 5 == 0:
        cadena_mult5_digitos += num_str
    
    # 2. Número es múltiplo de 5
    if num % 5 == 0:
        cadena_mult5_numeros += num_str
    
    # 3. Número contiene el dígito 100 (esto es imposible ya que 100 tiene 3 dígitos)
    # Interpretaré esto como que el número contiene "100" como substring
    if "100" in num_str:
        cadena_contiene_100 += num_str
    
    # 4. Número contiene el dígito 1
    if "1" in num_str:
        cadena_contiene_1 += num_str

# Añadir "UH" al final de cada cadena
cadena_mult5_digitos += "UH"
cadena_mult5_numeros += "UH"
cadena_contiene_100 += "UH"
cadena_contiene_1 += "UH"

# Mostrar resultados
print("\nResultados:")
print(f"1. Cadena con cantidad de dígitos múltiplo de 5: {cadena_mult5_digitos}")
print(f"2. Cadena con números múltiplos de 5: {cadena_mult5_numeros}")
print(f"3. Cadena con números que contienen '100': {cadena_contiene_100}")
print(f"4. Cadena con números que contienen '1': {cadena_contiene_1}")