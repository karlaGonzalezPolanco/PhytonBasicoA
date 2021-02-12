#Contraseña
contraseña = "contraseña"
pase = input("Ingrese la contraseña: ")

if contraseña == pase.lower():
    print("La contraseña ingresada es correcta.")
else:
    print("La contaseña ingresada es incorrecta.")

#Determinar sección del usuario
nombre = input("Ingrese el nombre del estudiante: ")
genero = input("Ingrese el género del estudiante (H o M): ")

if nombre.isalpha() and genero.isalpha():
    if genero == "M":
        if nombre.upper()  < "M":
            grupo = "A"
        else:
            grupo = "B"
    else:
        if nombre.upper() > "N":
            grupo = "A"
        else:
            grupo = "B"

    print(nombre + " debe estar en el grupo " + grupo)
else:
    print("Una de las entradas es incorrecta. Inténtelo de nuevo. ")