				
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



'''                                                ------------------------------  Tuplas  -------------------------------

¿Qué son las tuplas en Python?
Un tuple es una colección de datos cuyo orden es inalterable, o sea, son elementos ordenados en una secuencia específica y que posee importancia. 
En Python, los tuples se escriben entre paréntesis.
'''
# Ejemplo__1:

tupla = (4, "Hola" , 6.78,[1,2,3],4)

tupla.pop() # Esto en una tupla no funciona; Solo se puede buscar.

print(tupla)

# Ejemplo__2:

tupla = (4, "Hola", 6.78,[1,2,3],4)

print(tupla[2]) # Se puede seleccionar o mostrar 1 solo elemento (puede ser un índice positivo, 4 o índice -4)
print(tupla[1:]) # Esto tambien se puede hacer

# Ejemplo__3: Buscar --> Metodo IN

tupla = (4, "Hola", 6.78,[1,2,3],4)

print(4 in tupla)

# Ejemplo__3: Buscar --> Metodo ÍNDEX

tupla = (4, "Hola", 6.78,[1,2,3],4)

print(tupla.index("Hola"))
print(tupla.count(4))
print(len(tupla))


#																 Transformar/Convertir una Tupla en una Lista


tupla = (4, "Hola", 6.78,[1,2,3],4)
lista = list(tupla)

print(tupla)


#															 	  Transformar/Convertir una Lista en una Tupla

Lista = [4, "Hola", 6.78,[1,2,3],4]
lista = tuple(lista)

print(tupla)



'''                                               ------------------------------  Conjuntos -------------------------------

*Los conjuntos son grupos de elemtos desordenados; Donde no pueden haber duplicados
*Se pueden poner cualquier tipos de datos; Pero no se pueden poner otro tipo de colleciones dentro como (lista, tupla,etc)
*uno de los principales usos del tipo set es utilizarlo en operaciones del álgebra de conjuntos: unión, intersección, diferencia, diferencia simétrica,.

Un conjunto es una colección no ordenada de objetos únicos. 
Python provee este tipo de datos «por defecto» al igual que otras colecciones más convencionales como las listas, tuplas y diccionarios.

¿Cómo crear un conjunto en Python?
Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {} , o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable 
(como una lista, una tupla, una cadena …). Para crear un conjunto vacío, simplemente llama al constructor set() sin parámetros.

#La clase set ofrece cuatro métodos para eliminar elementos de un conjunto. Son: discard(), remove(), pop() y clear(). A continuación te explico qué hace cada uno de ellos.

*discard(elemento) y remove(elemento) eliminan elemento del conjunto. La única diferencia es que si elemento no existe, discard() no hace nada mientras que remove() 
lanza la excepción KeyError.

*pop() es un tanto peculiar. Este método devuelve un elemento aleatorio del conjunto y lo elimina del mismo. Si el conjunto está vacío, lanza la excepción KeyError.

*Finalmente, clear() elimina todos los elementos contenidos en el conjunto.

---------  set vs frozenset ------
En realidad, en Python existen dos clases para representar conjuntos: set y frozenset. 
La principal diferencia es que set es mutable, por lo que después de ser creado, se pueden añadir y/o eliminar elementos del conjunto, como veremos en secciones posteriores. 
Por su parte, frozenset es inmutable y su contenido no puede ser modificado una vez que ha sido inicializado.

*Para crear un conjunto de tipo frozenset, se usa el constructor de la clase frozenset():
'''
# -----  Ejemplo: SET()  ------

conjunto = set()

conjunto = {1,2,3, "Hola" ,4.56}

print(conjunto)

# Ejemplo__2: Agregando mas elementos al conjunto:

conjunto = set()

conjunto = {1,2,3, "Hola" ,4.56}

conjunto.add(5)       # esto como los conjuntos son desordenados y unicos no te va a agrega r al final sino que es aleatorio.
conjunto.add("Nahuel")

print(conjunto)


# Ejemplo__3: Eliminando elementos al conjunto:

conjunto = set()

conjunto = {1,2,3, "Hola" ,4.56}

conjunto.discard(3)       

print(conjunto)

# Otra forma pero para eliminar todos los elementos:

conjunto = set()

conjunto = {1,2,3, "Hola" ,4.56}

conjunto.clear()       

print(conjunto)

# Ejemplo__4: Buscar un determinado elemento:

conjunto = set()

conjunto = {1,2,3, "Hola" ,4.56}
      
print(2 in conjunto)

# Otra forma pero para saber si NO esta dentro del conjunto:

conjunto = set()

conjunto = {1,2,3, "Hola" ,4.56}
      
print(2 not in conjunto)

# Ejemplo__5: Como saber cuantos elementos tiene:

conjunto = set()

conjunto = {1,2,3, "Hola" ,4.56}
      
print(len(conjunto))

	
#																			CONJUNTOS SEGUNDA PARTE

# ----- Como hacer la igualdad de 2 conjuntos -----

a = {1,2,3}
b = {3,4,5}

print(a == b) # False

# Ejemplo-True

a = {1,2,3}
b = {3,1,2}

print(a == b) # True


'''																			 Unión de 2 conjuntos		

La unión de dos conjuntos A y B es el conjunto A ∪ B que contiene todos los elementos de A y de B.

En Python se utiliza el operador | para realizar la unión de dos o más conjuntos.	
'''
# Ejemplo:

a = {1,2,3}
b = {3,4,5}

c = a | b 

print(c)	# El 3 sale una vez porque no pueden haver duplicados. 	


'''                                                                       Intersección de conjuntos

La intersección de dos conjuntos A y B es el conjunto A ∩ B que contiene todos los elementos comunes de A y B.

En Python se utiliza el operador & para realizar la intersección de dos o más conjuntos.
'''
# Ejemplo:

a = {1,2,3}
b = {3,4,5}

c = a & b 

print(c)


'''                                                                         Diferencia de conjuntos             

La diferencia entre dos conjuntos A y B es el conjunto A \ B que contiene todos los elementos de A que no pertenecen a B.

En Python se utiliza el operador - para realizar la diferencia de dos o más conjuntos.
'''
# Ejemplo:

a = {1,2,3}
b = {3,4,5}

c = a - b 

print(c)   


'''                              								        Diferencia simétrica de conjuntos	

La diferencia simétrica entre dos conjuntos A y B es el conjunto que contiene los elementos de A y B que no son comunes.

En Python se utiliza el operador ^ para realizar la diferencia simétrica de dos o más conjuntos. ( Alt Gr + {} 2 veces = ^)
'''
# Ejemplo:

a = {1,2,3}
b = {3,4,5}

c = a ^ b 

print(c)   


'''                              								        Como saber si es un Subconjunto

¿Qué es un subconjunto en programación?
La teoría nos dice que A es subconjunto de B cuando A está incluido en B, que es lo mismo que decir que B contiene a A. 
Para finalizar, unas palabras sobre el concepto de conjuntos disjuntos. 
Sabemos que dos conjuntos son disjuntos cuando no tienen elementos en común, es decir, su intersección es el conjunto vacío.	


#																				  ISSUBSET()			

El método issubset() devuelve True si todos los elementos de un conjunto A están presentes en otro conjunto B que se pasa como argumento y devuelve falso si todos los elementos 
no están presentes.
'''
# Ejemplo:

a = {1,2,3}
b = {3,4,5}

c = {1,2,3,4,5}

print(a.inssubset(c))
print(b.inssubset(c))

'''																				  ISSUPERSET()

El método issuperset() devuelve True si todos los elementos de un conjunto A ocupan el conjunto B que se pasa como argumento y devuelve falso si todos los elementos de B no 
están presentes en A.
Esto significa que si A es un superconjunto de B, entonces devuelve verdadero; más falso
'''
# Ejemplo:

a = {1,2,3}
b = {3,4,5}

c = {1,2,3,4,5}

print(c.issuperset(a))

'''                                                                                 ISDISJOINT() 

Se dice que dos conjuntos están separados cuando su intersección es nula. 
En palabras simples, no tienen ningún elemento común entre ellos.
'''
# Ejemplo:

a = {1,2,3}
b = {3,4,5}

c = {1,2,3,4,5}

print(a.isdisjoint(b))


'''                              								                 Conjuntos inmutables


#																					  Frozenset

Al igual que las listas encuentran en las tuplas su versión inmutable, los conjuntos, que como vimos quedaban representados por el tipo set, hallan su inalterabilidad a través del 
tipo frozenset.

Podríamos traducir frozenset por algo así como conjunto congelado, término que muestra claramente su carácter estático. Podemos pensar en un frozenset como en un set en el que no 
podemos modificar su composición una vez creado.

Objetivo: presentar el tipo frozenset para la implementación de conjuntos inmutables.
'''
# Ejemplo:

a = frozenset({1,2,3})
b = {3,4,5}

print(a.isdisjoint(b))



'''                                                ------------------------------  Diccionarios  -------------------------------

Son otro tipo de colleción donde los elementos tambien se guardan desordenados; 
Pero la principal caracteristica es que tienen 2 elementos por posición (la CLAVE y el VALOR), y en estos No pueden haber claves duplicadas.

Los diccionarios en Python nos permiten almacenar una serie de mapeos entre dos conjuntos de elementos, llamados keys and values (Claves y Valores). 
Todos los elementos en el diccionario se encuentran encerrados en un par de corchetes {} .
'''
# Ejemplo: Traducción de colores de Español a Ingles

diccionario = {"azul":"blue" , "rojo":"red" , "verde":"green"}

print(diccionario["azul"])

'''                                                                    Agregar nuevos elementos al diccionario

Para definir un diccionario, se encierra el listado de valores entre llaves. 
Las parejas de clave y valor se separan con comas, y la clave y el valor se separan con dos puntos.
'''
# Ejemplo:

diccionario = {"azul":"blue" , "rojo":"red" , "verde":"green"}

diccionario["amarillo"] = "yellow"

print(diccionario) 

#																         	  Modificar elementos
# Ejemplo:

diccionario = {"azul":"blue" , "rojo":"red" , "verde":"green"}

diccionario["azul"] = "BLUE"

print(diccionario) 

#																			  Eliminar elementos
# Ejemplo:

diccionario = {"azul":"blue" , "rojo":"red" , "verde":"green"}

del(diccioanrio["verde"])

print(diccionario) 

#													 Insertar una (Lista o Tupla u otro diccionario) dentro de un Diccionario
# Ejemplo: Agenda secilla

diccionario = {"Nahuel": {"edad":18,"estatura":1.75}, "Jose":[21,1.78], "María":[22,1.67]}

print(diccionario["Nahuel"])


#																			DICCIONARIOS SEGUNDA PARTE

#																	Mostrar el valor al que pertenece la clave

# Ejemplo: equipo de futbol (número de la remera y a que jugador pertenece ese número) Equipo --> Selección Argentina
# De esta forma si le asignamos un valor que no tiene clave nos va a tirar un error

equipo = {10:"Leonel Messi", 11:"Ángel Di María", 7:"Rodrigo De Paul", 23:"Emiliano Martínez"}

print(equipo[10]) 

'''																						GET()

Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none.
'''
# Ejemplo__2:
# De esta forma si le asignamos un valor que no tiene clave nos va a tirar un mensaje personalizado

equipo = {10:"Leonel Messi", 11:"Ángel Di María", 7:"Rodrigo De Paul", 23:"Emiliano Martínez"}

print(equipo.get(6, "no existe ese número de camiseta")) 



#																	  Busqueda directa dentro del diccionario
# Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
# Ejemplo:

equipo = {10:"Leonel Messi", 11:"Ángel Di María", 7:"Rodrigo De Paul", 23:"Emiliano Martínez"}

print(10 in equipo) 

'''																					  KEYS()

Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
'''
# Ejemplo__3: quiero que me muestre solo el número de los jugadores

equipo = {10:"Leonel Messi", 11:"Ángel Di María", 7:"Rodrigo De Paul", 23:"Emiliano Martínez"}

print(equipo.keys()) 

'''																					VALUES()

Retorna una lista de elementos, que serán los valores de nuestro diccionario. 
'''
# Ejemplo__4: quiero que muestre solo los nombres

equipo = {10:"Leonel Messi", 11:"Ángel Di María", 7:"Rodrigo De Paul", 23:"Emiliano Martínez"}

print(equipo.values()) 

'''																					 ITEMS()		

Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.
'''
# Ejemplo__5: 

equipo = {10:"Leonel Messi", 11:"Ángel Di María", 7:"Rodrigo De Paul", 23:"Emiliano Martínez"}

print(equipo.tuplas()) 

'''																					   LEN()

El método len() devuelve la longitud de un objeto, ya sea una lista, una cadena, una tupla o un diccionario. 
len() toma un argumento, que puede ser una secuencia (como una cadena, bytes, tupla, lista o rango) o colección (como un diccionario, conjunto o conjunto "set" congelado "set frozen").
'''
# Ejemplo__6: quiero saber cuantos jugadores hay en mi equipo

equipo = {10:"Leonel Messi", 11:"Ángel Di María", 7:"Rodrigo De Paul", 23:"Emiliano Martínez"}

print(len(equipo)) 

'''																					  CLEAR()	
Elimina todos los ítems del diccionario dejándolo vacío.
'''
# Ejemplo__7: quiero sacar a todo mi equipo

equipo = {10:"Leonel Messi", 11:"Ángel Di María", 7:"Rodrigo De Paul", 23:"Emiliano Martínez"}

equipo.clear()

print(equipo)

'''                                                                      Otros Métodos de los Diccionarios

*Link --> https://devcode.la/tutoriales/diccionarios-en-python/
 
 Método       Descripción
dict ()       Recibe como parámetro una representación de un diccionario y si es factible, devuelve un diccionario de datos.
zip()         Recibe como parámetro dos elementos iterables, ya sea una cadena, una lista o una tupla. Ambos parámetros deben tener el mismo número de elementos. 
-             Se devolverá un diccionario relacionando el elemento i-esimo de cada uno de los iterables.
copy()        Retorna una copia del diccionario original.
fromkeys()    Recibe como parámetros un iterable y un valor, devolviendo un diccionario que contiene como claves los elementos del iterable con el mismo valor ingresado. 
-             Si el valor no es ingresado, devolverá none para todas las claves.
pop()		  Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.
setdefault()  Funciona de dos formas. En la primera como get (valor → 1 : nos sirve para agregar un nuevo elemento a nuestro diccionario.)
update()      Recibe como parámetro otro diccionario. Si se tienen claves iguales, actualiza el valor de la clave repetida; si no hay claves iguales, 
.             este par clave-valor es agregado al diccionario.

