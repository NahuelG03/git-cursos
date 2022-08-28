    ===============================================================================================================
	=                                                Curso de Python                                              =
    ===============================================================================================================

'''                          ==========================  Errores/Excepciones  ==========================

Existen 2 tipos de errores en python:
1- El primer gran bloque: Son los errores ocasionados por el programador.
2- EL segundo bloque: Son los errores cometidos por el usuario.


                              -------------------  Primer Bloque | Excepciones  -------------------

#                                                       Errores de sintaxis

Los errores de sintaxis, también conocidos como errores de interpretación, son quizás el tipo de queja más común que 
tenés cuando todavía estás aprendiendo Python:

El intérprete reproduce la línea responsable del error y muestra una pequeña “flecha” que apunta al primer lugar donde 
se detectó el error. El error ha sido provocado (o al menos detectado) en el elemento que precede a la flecha: 
en el ejemplo, el error se detecta en la función print(), ya que faltan dos puntos (':') antes del mismo. 
Se muestran el nombre del archivo y el número de línea para que sepas dónde mirar en caso de que la entrada venga de un programa.
'''
# Ejemplo:

while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax


#                                                       Errores semanticos

# Ejemplo: queremos sacar 4 elementos cuando tenemos solo 3.

lista = [1,2,3]

lista.pop()
lista.pop()
lista.pop()
lista.pop()

print(lista)

# Como prevenir estos errores

# Ejemplo: Condicionales

lista = [1,2,3]

while len(lista)>0:
    print(lista.pop())

print(lista)


# Ejemplo: Error de Index

lista = [1,2,3]

print(lista[5])

# Ejemplo: TypeError

numero = input("Digite un número: ") # No definimos el número (int o float), lo guarda como string.

print(f"La suma es: {numero+10}")


#                                                       Excepciones de usuario

# Ejemplo: ValueError, El usuario nos digita "uno"

numero = int(input("Digite un número: "))

print(f"La suma es: {numero+10}")


'''                                                              Try

La sentencia try funciona de la siguiente manera:

- Primero, se ejecuta la cláusula try (la(s) linea(s) entre las palabras reservadas try y la except).

- Si no ocurre ninguna excepción, la cláusula except se omite y la ejecución de la cláusula try finaliza.

- Si ocurre una excepción durante la ejecución de la cláusula try, se omite el resto de la cláusula. Luego, si su tipo coincide con 
la excepción nombrada después de la palabra clave except, se ejecuta la cláusula except, y luego la ejecución continúa después del bloque try/except.

- Si ocurre una excepción que no coincide con la indicada en la cláusula except se pasa a los try más externos; si no se encuentra un gestor,
se genera una unhandled exception (excepción no gestionada) y la ejecución se interrumpe con un mensaje como el que se muestra arriba.

Una declaración try puede tener más de una cláusula except, para especificar gestores para diferentes excepciones. Como máximo, se ejecutará un gestor. 
Los gestores solo manejan las excepciones que ocurren en la cláusula try correspondiente, no en otros gestores de la misma declaración try. 
Una cláusula except puede nombrar múltiples excepciones como una tupla entre paréntesis, por ejemplo:

... except (RuntimeError, TypeError, NameError):
...     pass

                                    
                                                                 Except
                                                               
Una clase en una cláusula except es compatible con una excepción si es de la misma clase o de una clase derivada de la misma (pero no de la otra manera — una cláusula 
except listando una clase derivada no es compatible con una clase base). Por ejemplo, el siguiente código imprimirá B, C y D, en ese orden:


                                                                  Else
                                                                  
ELse funciona directamente con el Except:
Cuando el except se ejecute o muestre el mensaje el Else no se va a ejecutar.
Esto quiere decir que cuando no haya ninguna excepción en el programa el Else se va a ejecutar, el lo contrario de except.   


                                                                 Finally             
                                                                 
El finally se va a ejecutar siempre con el Try y el Except, pero no con el Else 
Finally puede ser muy util para trabajar con base de datos para cerrar la conexión de la misma.                                                
'''
# Ejemplo: Manejo de excepciones, vamos a hacer que el programa no se detenga en el error si no que siga.

while True: # El while es opcional pero lo ponemos para que el programa no se detenga hasta que se ingrese un entero
    try: # Con Try queremos que intente resolver nuestro código

        numero = int(input("Digite un número: "))
        print(f"La suma es: {numero + 10}")
        break # Lo ponemos aca porque si el usuario pone un entero se muestre el resultado y listo y si encuentra una excepción siga el programa
    except: # Except va a capturar la excepción
           print("Ha ocurrido un error")


print("Programa terminado")

Ejemplo: sumamos Else y Finally

while True:
    try:
        numero = int(input("Digite un número: "))
        print(f"La suma es: {numero + 10}")
    except:
        print("Ha ocurrido un error")

    else:
        print("Programa finalizado correctamente")
        break

    finally:
        print("Iteración finalizada")

print("Programa terminado")
