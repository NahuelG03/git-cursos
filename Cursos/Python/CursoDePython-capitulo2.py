				
	========================================================================================================================================================================
	=                                                                        Curso de Python                                                                               =
    ========================================================================================================================================================================  				

'''                                            ==============================  Colecciones  =================================   

¿Qué es una colección en Python?
Una colección de datos en programación almacena 2 o más elementos en un arreglo con distintos números de índex, 
por lo que nos ayuda a agrupar elementos que tengan algo que ver unos con los otros. 
Existen cuatro tipos de colecciones de datos en el lenguaje Python: Lista es una colección ordenada y modificable. 


#                                                ------------------------------  Listas  -------------------------------

LINK: https://hetpro-store.com/TUTORIALES/listas-en-python-5-colecciones/

Las listas son algo parecido a lo que se conoce en otros lenguajes como Arreglos o Vectores;
En python las listas son estructuras de datos mas flexibles.

Una lista en Python es una estructura de datos formada por una secuencia ordenada de objetos. 
Los elementos de una lista pueden accederse mediante su índice, siendo 0 el índice del primer elemento.
La función len() devuelve la longitud de la lista (su cantidad de elementos).

Se pueden almacenar cualquier tipo de datos e incluso otras listas.

------ ¿Cómo hacer una lista en Python? -----

Para crear una lista en Python, debemos colocar todos los elementos que queramos añadir a esa lista entre corchetes [ ] y separados por comas. 
Las listas pueden contener cuantos elementos queramos y como ya decíamos, pueden ser de diferentes tipos (enteros, cadenas, booleanos, etc.)


 Metodo	           Descripción
append()	Añade un elemento al final de la lista
clear()	    Remueve todos los elementos de la lista
copy()	    Entrega una copoa de la lista
count()	    Entrega el número de elementos con un valor específico
extend()    Añade elementos de una lista (o cualquier iterable) al final de la lista actual
index()	    Entrega el número de índex del primer elemento con el valor especificado
insert()	Añade un elemento a la posición especificada
pop()	    Remueve el elemento de la posición especificada
remove()	Remueve el elemento con el valor especificado
reverse()	Invierte el orden de la lista
sort()	    Reacomoda la lista
'''
# Ejemplo: Lista días laborales y numeros. 

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",40,5.67,[1,2,3],True]

print(lista[1:4])

'''
Si deseamos obtener acceso a algún elemento en la lista, usaremos la siguiente indicación, colocando el número de índex (recordemos que en programación éstos comienzan en 0) 
que queremos imprimir entre los corchetes. 
También podemos pedirle al programa que lea el número de index de forma inversa añadiendo un signo «-» antes del número. Así, -1 se refiere al último elemento, -2 al penúltimo, etc.

- De igual manera, podemos imprimir un rango de elementos en la lista utilizando dos puntos : .
'''


'''								            	-----------------------  Longitud del arreglo | LEN()  --------------------------

Para determinar cuántos elementos contiene nuestra lista, utilizaremos la función len().
'''
# Ejemplo:

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",40,5.67,[1,2,3],True]

print(len(lista))

'''

#							                       	-----------------------  Añadir elementos  --------------------------

#																			     APPEND()

Además de sustituir, también podemos agregar más elementos a los ya existentes usando el comando append().
'''
# Ejemplo: 

lista = [1,2,3,4,5]
lista.append(6)
lista.append("Nahuel")

print(lista)

'''                                                                              INSERT()

Podemos incluso seleccionar el lugar en el que queremos añadir dicho objeto en la lista mediante el método insert().
'''
# Ejemplo:

lista = [1,2,4,5]
lista.insert(2,3) # Primero se le pasa en index donde queres que vaya (en este caso es 2) y despues el valor que quieras.

print(lista)



'''							                     	  -----------------------  Unir elementos --------------------------

#																				   EXTEND()

el método extend(), cuyo propósito es añadir los elementos de una lista a la otra.
'''
# Ejemplo: 

lista1 = [1,2,3,4,5]
lista2.extend(6,7,8) 

print(lista)


#																				   OPERADOR (+) 

# Ejemplo: 

lista1 = [1,2,3,4,5]
lista2.extend(6,7,8) 

lista3 = lista1 + lista2

print(lista3)

						
'''																		       	      APPEND

Otra manera es anexando los elementos de lista2 en la lista1, uno por uno.
'''
# Ejemplo:

lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

for x in lista2:
	lista1.append(x)

print(lista1)


'''			  	                            	   -----------------------  Verificar si un elemento existe --------------------------

#																						 IN

Esta función te permite conocer si un cierto elemento está presente en una lista.
'''
# ------  Ejemplo_1:  -------

lista = [1,2,3,4,5, "Nahuel"]

print("Nahuel" in lista)

# ------  Ejemplo_2:  -------
lista_frutas = ["fresa", "uva", "cereza"]
if "fresa" in lista_frutas:
	print("sí, 'fresa' se encuentra en la lista de frutas")


'''			  	                                -----------------------  En que índice se encuentra el elemento --------------------------

#																					   Índex()			

La lista de Python tiene un método incorporado llamado index() , que acepta un solo parámetro que representa el valor para buscar dentro de la lista existente. 
La función devuelve el índice de la primera aparición que encuentra a partir del índice 0 independientemente de cuántas veces se produzca dentro de la lista.
'''
# Ejemplo:

lista = [1,2,3,4,5, "Nahuel"] 

print(lista.index(5))


'''			  	                                 -----------------------  Cuanta veces aparece el elemento --------------------------

#																				        COUNT()

count() es una función incorporada en Python que devuelve el recuento de cuántas veces aparece un objeto dado en la lista. 
Parámetros: Objeto son las cosas cuya cuenta se va a devolver.
'''
# Ejemplo:

lista = [1,2,3,4,5, "Nahuel", 1,2,3,1, "Nahuel", 1]

print(lista.count(1))



'''			  	                                        -----------------------  Remover elementos --------------------------

Existen varios métodos para remover un elemento de una lista:
 *remove() -->  retira un elemento específico’
 *pop()  --> retira el número de índex especificado o o el último índex si no se especifica un número.
 *clear() --> Elimina todos los elementos de la lista.


'''#					  													          REMOVE()

# retira un elemento específico’
# Ejemplo:

lista = [1,2,3,4,5, "Nahuel"]
lista.remove(2)

print(lista)


'''																				   	     POP()

retira el número de índex especificado o o el último índex si no se especifica un número.
'''
# ------  Ejemplo__1: Elimina el ultimo elemento (Nahuel) ------

lista = [1,2,3,4,5, "Nahuel"]
lista.pop() 

print(lista)

# ------  Ejemplo__2: Elimina el index que le indicamos ------

lista = [1,2,3,4,5, "Nahuel"]
lista.pop(2)

print(lista)


'''                																	     CLEAR() 

Elimina todos los elementos de la lista.
'''
# Ejemplo:

lista = [1,2,3,4,5, "Nahuel"]
lista.clear()

print(lista)

'''			  	                                        -----------------------  Voltear una lista --------------------------

#																				  	 REVERSE()

Este método no devuelve un valor, sino una lista de los elementos será el orden inverso.
'''
# Ejemplo:

lista = [1,2,3,4,5, "Nahuel"]
lista.reverse()

print(lista)


'''			  	                                     -----------------------  Copiar todos los elementos --------------------------

#																				         *

Este metodo te va a copirar toda la lista y te la va a mostrar al lado de la original.
'''
# Ejemplo:

lista = [1,2,3,4,5, "Nahuel"]*2

print(lista)


'''			  	                                      -----------------------  Ordenar los elementos --------------------------

Las listas de Python tienen un método incorporado list. sort() que modifica la lista. 
También hay una función incorporada sorted() que crea una nueva lista ordenada a partir de un iterable. 

La forma más sencilla de ordenar una lista en Python es utilizar el método sort() de la clase list. 
Para listas que contienen elementos de tipos heterogéneos, llamar a la función sort() provocará que el intérprete lance un error.
'''
# -------  Ejemplo__1: Ordenamos los elementos de mayor a menor  -------

lista = [5,4,-7,9,0,1,3]

lista.sort()

print(lista)

# -------  Ejemplo__2: Ordenamos los elementos de menor a mayor  -------

lista = [5,4,-7,9,0,1,3]

lista.sort(reverse=True)

print(lista)


