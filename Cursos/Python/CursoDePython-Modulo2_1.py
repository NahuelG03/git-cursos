                ===============================================================================================================
	            =                                          Curso de Python | Modulo 2                                        =
                ===============================================================================================================



'''                                 ==========================  ARGUMENTOS  ==========================

¿Qué es un argumento en Python?
En la definición de una función los valores que se reciben se denominan parámetros, pero durante la llamada los valores que se envían se denominan argumentos.

Existen dos tipos de argumentos en Python: los convencionales y aquellos que están sujetos a un nombre específico, generalmente identificados como args (arguments) y 
kwargs (keyword arguments), respectivamente.
'''
# Ejemplo: Argumentos sujetos a un nombre
# script en Python que implemente un procedimiento para imprimir un genérico.
# El procedimiento deberá recibir el título del menú como primer argumento, seguido de las opciones a imprimir y finalmente parámetro con nombre para el mensaje de error
# en caso de una opción no válida .

def menu(titulo, *args, **kwargs):
    print(f'         {titulo}')
    for i in range(len(args)):
        print(f'{i+1} ) {args[i]}')
    opc = int(input('Selecciona una opción: '))
    if 1 <= opc <=len(args):
        print(f'Seleccionaste la opción {args[opc-1]}')
    else:
        print('Opción no válida')
        if 'error' in kwargs:
            print(f'{kwargs["error"]}')

menu('Operaciones aritméticas', 'Suma', 'Resta', 'Multiplicación',
error='No existe tal operación')

print('Nos vemos...')


'''                                  ==========================  MODULARIDAD  ==========================

La modularidad es, en programación modular y más específicamente en programación orientada a objetos, la propiedad que permite subdividir una aplicación en partes más 
pequeñas (llamadas módulos), cada una de las cuales debe ser tan independiente como sea posible de la aplicación en sí y de las partes restantes.
'''



'''                       ========================== Procedimiento MAIN(el principal) ==========================


la función main(), realmente, es un nombre para una función def establecida por convención entre los programadores de Python. Su traducción del inglés, 'principal', 
nos proporciona una pista clara de su razón de ser.

La función main() desempeña un doble papel: cuando elaboramos un programa, un script con varias funciones def en su interior, a veces se hace necesario proporcionar
un ORDEN DE JERARQUÍA al intérprete de Python para que éste sepa por qué función debe comenzar a ejecutarse nuestro script. A esta función es a la que llamamos main()
de tal modo que, cuando el programa comience a correr, se encuentre con una función con ese nombre, ejecutándola en primer lugar, y, de manera escalar, prosiga 
ejecutándose el resto de funciones en el orden en que hayamos dispuesto sus llamadas respectivas.

Como podemos deducir, la función main() establece un flujo de lectura propio alternativo al que Python desarrolla de manera predeterminada y que ya conocemos 
(de izquierda a derecha y, lo que nos interesa, de arriba a abajo).

Los archivos de Python se llaman módulos y se identifican mediante la extensión de archivo .py. Un módulo puede definir funciones, clases y variables.

Entonces, cuando el intérprete ejecuta un módulo, el variable __name__ se establecerá como __main__ si el módulo que se está ejecutando es el programa principal.

Pero si el código está importando el módulo desde otro módulo, entonces el variable __name__ se establecerá en el nombre de ese módulo. 
'''
# Ejemplo: script en Python que implemente un procedimiento para saludar al usuario de manera personalizada; el procedimiento deberá recibir el nombre del usuario como
# argumento.
# Se deberá crear otro procedimiento llamado " main " desde el cual se inicie la ejecución del programa y dentro del cual se solicite el nombre del usuario y se utilice
# el primer procedimiento descrito.

def saludo_personalizado(nombre):
    print(f'Gusto de verte {nombre}')

def main():
    usuario = input('¿Hola cómo te llamas? ')
    saludo_personalizado(usuario)

if __name__ == '__main__':
    main()


