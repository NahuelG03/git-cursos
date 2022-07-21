    ===============================================================================================================
	=                                                Curso de Python                                              =
    ===============================================================================================================

'''                          ==========================  FUNCIONES  ==========================

Las funciones son un bloque de código que van a estar dentro de nuestros programas y nos van a servir para resolver un
problema especifico dentro del programa. Ademas nos sirven para reutilizar el código las veces que queramos

Una función es un grupo de instrucciones que constituyen una unidad lógica del programa y resuelven un problema muy 
concreto.

tienen un doble objetivo:

- Dividir y organizar el código en partes más sencillas.
- Encapsular el código que se repite a lo largo de un programa para ser reutilizado.

puedes definir tus propias funciones para estructurar el código de manera que sea más legible y para reutilizar aquellas
partes que se repiten a lo largo de una aplicación. 
Esto es una tarea fundamental a medida que va creciendo el número de líneas de un programa.


Sintaxis:
En Python, una definición de función tiene las siguientes características:

1- La palabra clave def
2- Un nombre de función
3- Paréntesis ’()’, y dentro de los paréntesis los parámetros de entrada, 
   aunque los parámetros de entrada sean opcionales.
4- Dos puntos ’:’
5- Algún bloque de código para ejecutar
6- Una sentencia de retorno (opcional)



                              -------------------  Funciones sin retorno de valor  -------------------
                              
Estas funciones no retornan nada, simplemente estamos mostrando mensajes con print.
'''
# Ejemplo:

def saludar():   # En los paréntesis puede o no tener parámetros
    print("Hola amig@")

saludar()

# Ejemplo: Reutilizando la función (saludando 2 veces)

def saludar():
    print("Hola amig@")

saludar()
saludar()

# Ejemplo: PARÁMETROS (nombre del amig@)

def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Flor")
saludar("Carlos")

# Ejemplo: Tabla de multiplicar de 1 número

def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{num}*{i} = {num*i}")

tabla_multiplicar(5)
print()
tabla_multiplicar(3)


'''                              -------------------  Funciones con retorno de valor  -------------------

return se utiliza para establecer el resultado (o valor de retorno) de una función.

aunque solo puede usarse dentro de las funciones: no puede haber un return en cualquier otro lugar del código que no sea
el interior de una función.
'''
# Ejemplo: Multiplicación de 2 números

def multiplicar(num1,num2):
    mult = num1*num2
    return mult

print(multiplicar(3,4))

# Opción de retorno 2:

def multiplicar(num1,num2):
    mult = num1*num2
    return mult

mult = multiplicar(3,4)

print(mult)

# Ejemplo: Volviendo a llamar

def multiplicar(num1,num2):
    mult = num1*num2
    return mult

mult = multiplicar(3,4)

print(mult)

print(multiplicar(7,8))
print(multiplicar(3,9))

# Ejemplo: retorno de multiples valores

def prueba():
    return "hola",45,[1,2,3]

print(prueba())

# Otra forma es almacenarlos en variables: c = cadena, n = número, l = lista

def prueba():
    return "hola",45,[1,2,3]

c,n,l = prueba()

print(c)
print(n)
print(l)


'''                              -------------------   Argumentos y parámetros  -------------------

En la definición de una función los valores que se reciben se denominan parámetros, pero durante la llamada los valores 
que se envían se denominan argumentos.

 Parámetro:
Un parámetro es un valor que la función espera recibir cuando sea llamada (invocada), a fin de ejecutar acciones en base
al mismo. Una función puede esperar uno o más parámetros (que irán separados por una coma) o ninguno.

 Argumentos:
Los argumentos son los nombres de los valores pasados a una función por una llamada de función.
Existen dos tipos de argumentos en Python: los convencionales y aquellos que están sujetos a un nombre específico, 
generalmente identificados como args (arguments) y kwargs (keyword arguments)
'''
# Ejemplo: Restar 2 números (Argumentos por posición (4,3) = num1,num2)

def restar(num1,num2): # Parámetros
    return num1-num2

print(restar(4,3)) # Argumentos

# Ejemplo: Argumentos por nombre

def restar(num1,num2): # Parámetros
    return num1-num2

print(restar(num2=4,num1=2)) # Argumentos


'''                           -------------------   Argumentos por valor o por referencia  -------------------

Dependiendo del tipo de dato que enviemos a la función, podemos diferenciar dos comportamientos:

Paso por valor: Se crea una copia local de la variable dentro de la función.
Paso por referencia: Se maneja directamente la variable, los cambios realizados dentro de la función le afectarán 
también fuera.

    Tradicionalmente:

Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...


  ¿Qué es paso por valor de un argumento?
El paso de parámetros por valor consiste en copiar el contenido de la variable que queremos pasar en otra dentro del 
ámbito local de la subrutina, consiste pues en copiar el contenido de la memoria del argumento que se quiere pasar a 
otra dirección de memoria, correspondiente al argumento dentro del ámbito de dicha
'''
# Ejemplo: Doblar el valor de un número (paso por valor)

# Como ya sabemos los números se pasan por valor y crean una copia dentro de la función, por eso no les afecta
# externamente lo que hagamos con ellos:

def doblar_valor(numero):
    numero *= 2

n = 5
doblar_valor(n) # Aca estamos pasándole 'n' como argumento por valor; Esto significa que estamos pasándole una copia del
                # valor que tiene 'n' a la variable "numero"


# Ejemplo: modificar el valor original

def doblar_valor(numero):
    return numero*2

n = 5
n = doblar_valor(n)

print(n)


# Ejemplo: Paso por referencia (modificar el valor original)
# Sin embargo, las listas u otras colecciones, al ser tipos compuestos se pasan por referencia, y si las modificamos
# dentro de la función estaremos modificándolas también fuera:

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

n = [5,10,15,20]
doblar_valores(n)

print(n)

# Ejemplo: pasando a valor (en el caso de los tipos compuestos, podemos evitar la modificación enviando una copia)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

n = [5,10,15,20]
doblar_valores(n[:]) # [:] = copia

print(n)

