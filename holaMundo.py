# Ejercicio Uno. 
# Crear un programa que permita ingresar dos cadenas vía la consola y luego las compare,imprimiendo un mensaje en caso que sean
# iguales y otro en caso que sean diferentes.

# wordOne = input("Ingrese primera palabra: ")
# wordTwo = input("Ingrese la segunda palabra: ")

# if wordOne == wordTwo:
#     print("Las palabras son iguales")
# else:
#     print("Las palabras son diferentes")

# Ejercicio Dos.
# Crear un programa que solicite el nombre de un alumno a través de la consola, y luego chequee que no esté vacío.
# En caso de estarlo, tiene que imprimir un mensaje de error; caso contrario, deberá imprimir un mensaje indicando
# que se ingresó correctamente.

# alumno = input("Ingrese nombre del alumno: ")

# if alumno == "":
#     print("No ingreso el nombre correcto del almuno")
# else:
#     print(f"el nombre del alumno es {alumno}")

# Ejercicio Tres.
# Pedir la edad por teclado y comparar si es mayor o menor de edad. No olvidar de que para poder comparar el ingreso debe ser convertido a
# int, ya que el usuario ingresa un número entero.

# age = int(input("Ingrese un numero:"))

# print(type(age))

# if age < 18:
#     print("Eres menor de edad")
# elif age >= 18 and age<= 100:
#     print("Eres mayor de edad")
# elif age > 100:
#     print("Eres Longevo")

# Ejercicio Cuatro.
# Con un bucle while incrementar una variable entera de uno en uno (desde 0 a 10 sin incluir).
# Mostrar por pantalla el resultado por vuelta.

# var = 0
# while var < 10:
#     print (var) 
#     var = var + 1 

# Ejercicio Cinco.
# Pedir por teclado el nombre de usuario, si está vacío, volver a pedirlo hasta que se ingrese un nombre.
# Luego, saludar al usuario.

# nombre = input("Ingrese su nombre: ")
# while nombre == "":
#     nombre = input("Ingrese su nombre nuevamente: ")
# print(f"Hola {nombre}")

# Ejercicio Seis.
# Se tiene la siguiente lista de nombres: nombres = ["Susana","Alejandro","Roberto"]
# Insertar entre Alejandro y Roberto a Paula. Y luego agregar al final a Silvina.
# Para finalizar, hay que recorrer la lista y mostrar a todos los nombres por pantalla.


# nombres = ["Susana", "Alejandro", "Roberto"]
# nombres.append("Silvina") 
# nombres.insert(2,"Paula")
# print(nombres)

# indice = 0

# while indice < len(nombres):
#     print(nombres[indice])
#     indice = indice +1


# Ejercicio Siete.
# Recorrer lista con for Se tiene una lista de nombres y se desea recorrer con un bucle for.
# nombres = ["Agustina","Marisa","Juan","Osvaldo"]

# Ejercicio ocho.
# 1. Crear un programa que solicite una fila y una columna e imprima en pantalla el número en esa posición según la siguiente matriz:
# matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
# 2. El programa debe chequear que la fila y la columna tengan valores válidos.

matriz = [
         [3.3,6.1,4.0],
         [4.9,5.7,6.4]
         ]

fila    = int(input("Ingresar el numero de fila a acceder"))
columna = int(input("Ingresar el umero de columna a acceder"))

if fila < len(matriz):
    if columna < len(matriz[fila]):
        print(matriz[fila][columna])
    else:
        print("Error en las columnas")
else:
    print("error en las filas")






