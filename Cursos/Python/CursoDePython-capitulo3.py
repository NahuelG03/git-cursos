 
    ========================================================================================================================================================================
	=                                                                        Curso de Python                                                                               =
    ========================================================================================================================================================================   

'''                                            ==============================  Bucles | Ciclos  =================================    

Son simplemente un trozo de código que se va a repetir un número Indeterminado o Determinado de veces.

Un ciclo en Python o bucle en Python (como prefieras llamarlos) te permite repetir una o varias instrucciones cuantas veces lo necesitemos, 
por ejemplo, si quisiéramos escribir los números del uno al cien no tendría sentido escribir cien líneas de código mostrando un número en cada una, para eso y para varias cosas más ...

#                                                                  -----------  WHILE (Mientras)  -----------

* La sentencia while se usa para la ejecución repetida siempre que una expresión sea verdadera.

El bucle while evalúa una condición y luego ejecuta un bloque de código si la condición es verdadera. 
El bloque de código se ejecuta repetidamente hasta que la condición llega ser o es falsa.
'''
# Ejemplo: sacar la raíz cudrada de un número positivo, (vamos a usar el bucle while para estar seguros del que el número ingresado sea positivo)

import math # Importamos el modulo math para utilizar el sqrt y sacar la raíz cuadrada

numero = int(input("Digite un numero: "))

while numero<0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")


# Ejemplo__2: Mostrar un "hola mundo" 10 veces

i = 0 

while i<10:
    print("Hola mundo")
    i += 1 

# Ejemplo__3: Mostrar los numeros del 0 al 9

i = 0

while i<10:
    print(i)
    i += 1


'''                                                                    -----------  FOR()  -----------

El bucle FOR es conocido por tener un numero determinado de iteraciones.

La sentencia for se usa para iterar sobre los elementos de una secuencia (como una cadena de caracteres, tupla o lista) u otro objeto iterable.
'''
# Ejemplo: 

for i in [2,10,3,4,"Nahuel"]: # El bucle for te recorre la colección elemento por elemento
    print("Hola mundo")       # y depende cuantos elementos haya es la cantidad de veces que se va a repetir el bucle


# Ejemplo__2: Mostrar el valor de la variable iteradra (i)

for i in [2,10,3,4,"Nahuel"]:
    print(f"Elemento: {i}")

# otra forma:

coleccion = [2,10,3,4,"Nahuel"]

for i in coleccion:
    print(f"Elemento: {i}")


# Ejemplo__3: recorriendo un diccionario
# Sacando la clave

coleccion = {"Nahuel":22, "Maria":23, "Jose":45, "Luis":12}

for i in coleccion:
    print(f"Elemento: {i}")


# Sacando el valor

coleccion = {"Nahuel":22, "Maria":23, "Jose":45, "Luis":12}

for i in coleccion:
    print(f"{coleccion[i]}")


# sacando la clave y el valor

coleccion = {"Nahuel":22, "Maria":23, "Jose":45, "Luis":12}

for i in coleccion:
    print(f"{i} -> {coleccion[i]}")

# Otra forma

coleccion = {"Nahuel":22, "Maria":23, "Jose":45, "Luis":12}

for clave, valor in coleccion.items():
    print(f"{clave} -> {valor}")


# Recorriendo cadenas

coleccion = "Nahuel"

for i in coleccion:
    print(f"{i}")

# recorrido: resultado en una línea

coleccion = "Nahuel"

for i in coleccion:
    print(f"{i}",end=" ")



'''                                                                  -----------  Bucle FOR tipo RANGE   -----------

 la función incorporada range() retorna un iterador de enteros adecuado para emular el efecto de Pascal for i := a to b do; por ejemplo, list(range(3)) retorna la lista [0, 1, 2].
'''
# Ejemplo: hacer que el bucle for haga 50 repeticiones

for i in range(50):
    print(i)

# Ejemplo__2: mostrar los numeros del 5 al 10

for i in range(5,11):
    print(i)

# Ejemplo__3: mostrar numeros pares del 2 al 20

for i in range(2,21,2): # La sintacxis seria haci (De donde va a comenzar, Hasta donde va a llegar, y de cuanto en cuanto va a aumentar.(en este caso seria 2))
    print(i)

# Otra forma

for i in range(20,1,-2):
    print(i)



'''                                                             -----------   Instrucción CONTINUE y BREAK   -----------

Estas 2 instrucciones se pueden usar en todos los bucles que vimos: While, For, For-range

-La sentencia break ejecutada en la primera suite termina el bucle sin ejecutar el conjunto de cláusulas else. 
-La sentencia continue ejecutada en la primera suite omite el resto de las cláusulas y continúa con el siguiente elemento, o con la cláusula else si no hay un elemento siguiente.
'''
# Ejemplo__Range: crear un bucle que muestre los numeros del 0 al 9, que cuando llegue al 5 lo salteé y continue con los otros

for i in range(10):
    if i==5:
        continue # esta funcion no llega al print sino que cuando ve que cumple la condicion este regresa al principo y saltea el numero
    print(i)

# Ejemplo__Breack: crear un bucle que muestre los numeros del 0 al 9, que cuando llegue al 5 se detenga el programa

for i in range(10):
    if i==5:
        break # esta funcion hace que cuando se cumpla una condicion se tome un break "descanso" y se cierre el programa
    print(i)
print("Programa finalizado")






