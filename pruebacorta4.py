#Escriba un programa que solicite al usuario 7 nombres o apellidos y los almacene en una lista.
#Mostrar en pantalla verdadero si: todos los nombres o apellidos de las personas comienzan con la misma
#letra o si terminan con la misma letra, de lo contrario mostrar False.
#Por ejemplo, si fueran solo 2 nombres ingresados los solicitados Jorge y Jose, se mostrará True, ya que
#ambos comienzan con la misma letra.
#Si los nombres son Pablo y Marco se mostrará True, ya que ambos terminan con la misma letra.
#Si los nombres son Claudio y Lorena se mostrará False, ya que no coinciden ni la primera ni la última letra.


# Solicitar al usuario 7 nombres o apellidos
print("Favor ingrese 7 nombres o apellidos:")
nombres_apellidos = []
for i in range(7):
      print(f"El nombre o Apellido es el número {i+1}")
      nombre1 = input(f"Ingrese el nombre o apellido {i+1}:")
      nombres_apellidos.append(nombre1)

# Verifica si todos comienzn con la misma leta
primera_letra = nombres_apellidos[0][0].lower()  # se toma la primer letra del primer nombre
comienzan_igual =    all(nombre1[0].lower() == primera_letra for nombre1 in nombres_apellidos)

# verificar si todos terminan con la mima letra
ultima_letra = nombres_apellidos[0][-1].lower()  # Tomamos la última letra del primer nombre
terminan_igual =   all(nombre1[-1].lower() ==   ultima_letra for nombre1 in nombres_apellidos)

# Mostrar True si alguno de los dos casos se cumpl False si no
#print("comienzan igual" or "terminan_igual")
print(comienzan_igual or terminan_igual)