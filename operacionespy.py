def fibonacci(n, limite=0):
    fn1=1
    fn2=1
    limiteDinamico = limite-3    
    if n==1:
        print('0')
    elif n==2:
        print('0','1', end=" ")
    else:
        print('0', end=" ")
        print(fn1, end=" ")
        print(fn2, end=" ")
        for i in range(n-3):
            total = fn1 + fn2
            fn2=fn1
            fn1= total
            if ( (limite > 0) and (i >= (limiteDinamico)) ):
                break
            print(total, end=" / ")            
            #print(total, "i:",i, "b:", (i >= (limiteDinamico)))
           
 
#fb(99, 100)  # Cambia el segundo parámetro para establecer un límite  
#fb(101, 100)  # Cambia el segundo parámetro para establecer un límite  
         
def main():
    #print(fibonacci(9, 10))
    #print("------------------------------")
    #print(fibonacci(11, 10))
   
    numero=int(input("Ingrese el numero al cual se le calculara el fibonacci: "))
    if numero >= 100:
        print("No soportamos secuencias de Fibonacci mayores a 100")
    else:
        fibonacci(numero,29)
 
if __name__ == "__main__":
    main()
 