import msvcrt
import os

class JugadorLoteria:
    def __init__(self, nombre, cedula, usuario, clave, numeros):
        """
       JugadorLoteria
        """
        self.nombre = nombre
        self.cedula = cedula
        self.usuario = usuario
        self.clave = clave
        self.numeros = numeros
    def __str__(self):
        """
        Método para representar el objeto como string
        """
        numeros_str = ', '.join(map(str, self.numeros))
        return (f"Jugador: {self.nombre}\n"
                f"Cédula: {self.cedula}\n"
                f"Usuario: {self.usuario}\n"
                f"Clave: {self.clave}\n"
                f"Números a jugar: {numeros_str}\n"
                f"{'-' * 40}")

def verificar_tecla_esc():
    """
    verificar si se presionó la tecla ESC
    """
    if msvcrt.kbhit():
        tecla = msvcrt.getch()
        if tecla == b'\x1b': 
            return True
    return False

def leer_dato(mensaje, tipo=str):
    """
leer un dato con verificación tecla ESC
    """
    print(mensaje, end='', flush=True)
    valor = input()
    
    # Verificar si se presionó ESC durante la entrada
    if verificar_tecla_esc():
        print("\n¡Tecla ESC detectadaSaliendo del programa.")
        exit()
    
    return tipo(valor) if valor else valor

def leer_numeros_loteria():
     """
     leer los números de lotería (6 números entre 1 y 50)
     """
     numeros = []
     print("Ingrese 6 númeos para jugar (entre 1 y 50):")
    
     for i in range(6):
        while True:
            try:
                if verificar_tecla_esc():
                    print("\n¡Tecla ESC detectada! Saliendo del programa...")
                    exit()
                
                numero = leer_dato(f"Número {i+1}: ", int)
                
                if numero < 1 or numero > 50:
                    print("Error: el número debe estar entre 1 y 50")
                    continue
                
                if numero in numeros:
                    print("Error: número repetido")
                    continue
                
                numeros.append(numero)
                break
                
            except ValueError:
                print("Error: ingrese un número válido")
    
     return sorted(numeros)
def crear_jugador(numero_jugador):
    """
    crear un jugador con todos sus datos
      """
    print(f"\n{'='*50}")
    print(f"INGRESO DE DATOS-JUGADOR {numero_jugador}")
    print(f"{'='*50}")
    nombre = leer_dato("Nombre completo= ")
    cedula = leer_dato("Cédula= ")
    usuario = leer_dato("Usuario= ")
    clave = leer_dato("Clave= ")
    numeros = leer_numeros_loteria()
    return JugadorLoteria(nombre, cedula, usuario, clave, numeros)
def main():
    """
    Función prprinpal del programa
    """
    print("SISTEMA DE REGISTRO DE JUGADORES DE LOTERia")
    print("Presione ESC para salir")
    print()
    jugadores = []
    cantidad_jugadores = 7
    
    for i in range(cantidad_jugadores):
        try:
            jugador = crear_jugador(i + 1)
            jugadores.append(jugador)
            
        except SystemExit:
            # Salir si se detectó ESC
            return
        except Exception as e:
            print(f"Error al crar jugador: {e}")
            continue
    
 # Mostrar todos los jugadores registrados
    print(f"\n{'='*60}")
    print("JUGADORES REGISTRADOS Ssistema de Lotería")
    print(f"{'='*60}")
    
    for i, jugador in enumerate(jugadores, 1):
        print(f"\nJugar #{i}")
        print(jugador)

if __name__ == "__main__":
    main()