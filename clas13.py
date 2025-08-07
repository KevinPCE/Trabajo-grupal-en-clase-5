def inicializar_cadenas():
    """Inicializa y retorna las cuatro cadenas vacías"""
    return {"mult5_digitos": "", "mult5_numeros": "", "contiene_100": "", "contiene_1": ""}

def procesar_numero(numero, cadenas):
    """Procesa un número y lo agrega a las cadenas correspondientes según los criterios"""
    num_str = str(numero)
    num_int = int(numero)
    
    # 1. Cantidad de dígitos múltiplo de 5
    if len(num_str) % 5 == 0:
        cadenas["mult5_digitos"] = agregar_a_cadena(cadenas["mult5_digitos"], num_str)
    
    # 2. Número múltiplo de 5
    if num_int % 5 == 0:
        cadenas["mult5_numeros"] = agregar_a_cadena(cadenas["mult5_numeros"], num_str)
    
    # 3. Contiene el número 100
    if "100" in num_str:
        cadenas["contiene_100"] = agregar_a_cadena(cadenas["contiene_100"], num_str)
    
    # 4. Contiene el dígito 1
    if "1" in num_str:
        cadenas["contiene_1"] = agregar_a_cadena(cadenas["contiene_1"], num_str)
    
    return cadenas

def agregar_a_cadena(cadena, numero):
    """Agrega un número a una cadena existente con formato de separación por comas"""
    if cadena:
        return f"{cadena}, {numero}"
    return numero

def debe_terminar(numero):
    """Determina si el programa debe terminar basado en el número ingresado"""
    num_int = int(numero)
    return num_int % 20 == 0 or num_int < 0

def mostrar_resultados(cadenas):
    """Muestra los resultados formateados con el terminador UH"""
    print(f"Números cuya cantidad de dígitos es múltiplo de 5: {cadenas['mult5_digitos']}, UH")
    print(f"Números que son múltiplos de 5: {cadenas['mult5_numeros']}, UH")
    print(f"Números que contienen el 100: {cadenas['contiene_100']}, UH")
    print(f"Números que contienen el 1: {cadenas['contiene_1']}, UH")

def main():
    """Función principal que orquesta todo el programa"""
    cadenas = inicializar_cadenas()
    
    while True:
        numero = input("Número: ")
        
        if debe_terminar(numero):
            break
        
        try:
            cadenas = procesar_numero(numero, cadenas)
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue
    
    mostrar_resultados(cadenas)

if __name__ == "__main__":
    main()