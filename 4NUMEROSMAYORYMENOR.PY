def número_mayor():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    num4 = int(input("Ingrese el cuarti número"))

    if num1 > num2 and num1> num3 and num1> num4:
        print(f"El valor mayor es: {num1}")
    elif num2 > num1 and num2> num3 and num2> num4:
        print(f"El valor mayor es: {num2}")
    elif num3> num1 and num3> num2 and num3> num4:
        print(f"El valor mayor es: {num3}")
    elif num4> num1 and num4> num2 and num4> num3:
        print(f"El valor mayor es: {num4}")

    