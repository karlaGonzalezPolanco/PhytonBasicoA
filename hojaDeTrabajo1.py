

#Determinar si un número es primo
n = input("Introduce un número entero positivo: ")
i = 2
try: 
    n = int(n)
    if n <= 0:
        print("El número ingresado debe ser positivo. ")
    elif n == 1:
        print("El número 1 no se considera primo ni compuesto. ")
    else:
        while n % i != 0:
            i += 1
        if i == n:
            print(str(n) + " es primo")
        else:
            print(str(n) + " no es primo")   
except ValueError:
    print("El valor ingresado no es un número entero.")

    