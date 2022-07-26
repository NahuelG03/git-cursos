    ===============================================================================================================
	=                                                Curso de Python                                              =
    ===============================================================================================================

'''                          ==========================  CADENAS  ==========================

Los cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. 
Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.


                              -------------------  Cadenas de caracteres  -------------------

Las cadenas en Python o strings son un tipo inmutable que permite almacenar secuencias de caracteres. 
Para crear una, es necesario incluir el texto entre comillas dobles " . 
Puedes obtener más ayuda con el comando help(str). 
También es valido declarar las cadenas con comillas simples simples ' .
'''
# Ejemplo: (Comillas "")

cadena = "Hola mundo"

print(cadena)

# Ejemplo: (Comillas '')

cadena = 'Hola mundo'

print(cadena)

# Ejemplo: Combinadas (Se puede al revés también)

cadena = "Estoy 'estudiando'"

print(cadena)

# Ejemplo: Usando solo comillas ""

cadena = "Estoy \"estudiando\"" # Para que no me borre lo que está entre comillas(estudiando) lo envuelvo en \

print(cadena)

# Ejemplo: Cadena con muchos espacios

cadena = "Estoy \testudiando" # \t = 1 TAB

print(cadena)

# Ejemplo: Salto de línea

cadena = "Estoy \nestudiando"

print(cadena)

# Ejemplo: Mensaje en crudo (Ubicación de la computadora)

cadena = r"D:\nombre\trabajos" # R te lo imprime tal como esta

print(cadena)

# Ejemplo: Cadenas en muchas líneas

cadena = """Hola
que tal?
Mi nombre es Nahuel
"""

print(cadena)

# 0tra forma solo con Print()

print("""Hola
que tal?
Mi nombre es Nahuel
""")

# Ejemplo:

cadena1 = "Hola "
cadena2 = "Que tal?"

print(cadena1 + cadena2)


'''                            -------------------   Indices y slicing  -------------------

¿Qué es Indexing en Python?
index() devuelve la primera aparición / índice del elemento en la lista dada como argumento de la función.

¿Qué es el slicing en Python?
La expresión slicing hace referencia a la operación por medio de la cual se extraen elementos de una secuencia, 
tal como una lista o una cadena de caracteres. 
Dependiendo del caso, los elementos podrían ser consecutivos o podrían estar separados dentro de la secuencia original.
'''
# Ejemplo: Indices (Se pueden negativos y positivos)

cadena = "Nahuel"

print(cadena[1])

# Ejemplo: Slicing (Desde:Hasta - 1)

cadena = "Nahuel"

print(cadena[1:4])

# Ejemplo: Desde el inicio hasta el final y al revés

cadena = "Nahuel"

print(cadena[1:])
# Al revéz
print(cadena[:4])

# Ejemplo: cambiar o agregar valor

cadena = "Nahuel"

cadena[0] = 'h'

print(cadena) # ERROR no se puede de esta forma porque son inmutables

cadena = "Nahuel"

cadena = 'h' + cadena[1:]

print(cadena)

# Ejemplo: Calcular la cantidad de caracteres

cadena = "Nahuel"

print(len(cadena))


'''                            -------------------   Métodos para cadenas  -------------------


                                                            upper()
                                                            
Con este método conseguiremos convertir todos y absolutamente todos los caracteres de un string en mayúsculas, 
da igual lo largo que sea.                                                                                                                                     
'''
# Ejemplo:

cadena = "hola mundo".upper()

print(cadena)

# Otra forma:

cadena = "hola mundo"

print(cadena.upper())


'''                                                         lower()

Y como gemelo opuesto pero no malvado, tenemos el método lower() que hace exactamente lo contrario, 
lo convierte todo en minúsculas.
'''
# Ejemplo:

cadena = "HOLA MUNDO".lower()

print(cadena) # También se puede colocar aca el método


'''                                                       capitalize()

El método capitalize() de la clase de cadena pone en mayúscula el primer carácter, mientras que los caracteres restantes
son minúsculas. 
No hace nada si el primer carácter ya está en mayúsculas.
'''
# Ejemplo:

cadena = "hola mundo".capitalize()

print(cadena)


'''                                                          title() 

El método title() habilita el título de cada palabra en mayúsculas y minúsculas. 
Significa que el primer carácter de cada palabra se convierte a mayúsculas y los caracteres restantes de la palabra se 
convierten a minúsculas.
'''
# Ejemplo:

cadena = "hola mundo".title()

print(cadena)


'''                                                          count()

método count () se utiliza para contar el número de veces que un elemento que aparece en la lista.
'''
# Ejemplo: Contando la letra o

cadena = "hola mundo".count('o') # Se tiene que especificar lo que queremos contar

print(cadena)

# Ejemplo: Contando la palabra "Mundos"

cadena = "hola mundo mundo mundo".count('mundo')

print(cadena)


'''                                                          find()

SINTAXIS
str.find(sub[, start[, end]])

El método str.find devuelve el índice más bajo en el que se encuentre el substring sub en el bloque str[start:end]. 
Si el substring sub no se encuentra, devuelve el valor -1. Si no se especifican los argumentos start o end, se toman 
como valores por defecto el comienzo y el final del string. 
Si, por el contrario, se especifican, el substring a buscar deberá encontrarse completo dentro del rango.
'''
# Ejemplo: En que índice está la primera letra u

cadena = "hola mundo mundo mundo".find('u')

print(cadena)

# Ejemplo: En que índice está la primera palabra "mundo"

cadena = "hola mundo mundo mundo".find('mundo')

print(cadena)

# Ejemplo: Encontrar la última coincidencia (mundo)

cadena = "hola mundo mundo mundo".rfind('mundo') # r = reverse

print(cadena)


'''                                                          isdigit()

El método isdigit() se usa para detectar una cadena que consta de sólo números.

El método isdigit() devuelve "Verdadero" si todos los caracteres de la cadena son dígitos. 
De lo contrario, devuelve "False". 
Esta función se usa para verificar si el argumento contiene dígitos como: 0123456789
'''
# Ejemplo: True

cadena = "1000".isdigit()

print(cadena)

# Ejemplo: False

cadena = "1000A".isdigit()

print(cadena)


'''                                                          isalpha()

El método isalpha() se usa para detectar la cadena se compone de sólo letras.

Los métodos isalpha() devuelven "Verdadero" si todos los caracteres de la cadena son alfabetos. 
De lo contrario, devuelve "False".
Esta función se usa para verificar si el argumento incluye solo caracteres alfabéticos.
'''
# Ejemplo: True

cadena = "AsqT".isalpha()

print(cadena)

# Ejemplo: False

cadena = "AsqT140".isalpha()

print(cadena)


'''                                                          isalnum()

El método isalnum comprueba si la cadena es alfanumérica.
 
es decir, si los caracteres que la componen son solo letras y/o números y tiene al menos un carácter. 
Devuelve True en caso afirmativo. 
Devuelve False si no es alfanumérica o está vacía.
'''
# Ejemplo: True

cadena = "AsqT1".isalnum()

print(cadena)

# Ejemplo: False

cadena = "AsqT1=".isalnum()

print(cadena)


'''                                                          islower()

El método islower devuelve True cuando todos los caracteres alfabéticos que componen la cadena están en minúscula.

Puede contener todo tipo de caracteres, pero solo comprobará los alfabéticos. 
Devolverá False si al menos uno de los caracteres alfabéticos está en mayúscula o si no hay ningún carácter alfabético.
'''
# Ejemplo: True

cadena = "hola mundo".islower()

print(cadena)


'''                                                          isupper()

El método isupper() se usa para detectar si una cadena de todas las letras aparecen en mayúsculas.
'''
# Ejemplo: True

cadena = "HOLA MUNDO".isupper()

print(cadena)


'''                                                          istitle()

El método istitle() se usa para detectar todas las palabras estén escritas cadena es una primera letra mayúscula y otras
letras en minúsculas.

Istitle() devuelve True si la cadena es una cadena con título; de lo contrario, devuelve False.
'''
# Ejemplo: True

cadena = "Hola Mundo".istitle()

print(cadena)

# Ejemplo: False

cadena = "Hola mundo".istitle()

print(cadena)



'''                                                          isspace()

El método isspace() se usa para detectar la cadena se compone de sólo espacios.

Los métodos isspace() devuelven "Verdadero" si todos los caracteres de la cadena son espacios en blanco. 
De lo contrario, devuelve "False".

Esta función se usa para verificar si el argumento contiene todos los caracteres de espacio en blanco como:

# ' ' - Espacio
# '\ t': pestaña horizontal
# '\ n' - Nueva línea
# '\ v': pestaña vertical
# '\ f' - Feed
# '\ r' - Retorno de carro
'''
# Ejemplo: True

cadena = "          ".isspace()

print(cadena)

# Ejemplo: False

cadena = "     x    ".isspace()

print(cadena)



'''                            -------------------   Métodos para cadenas (Parte 2)  -------------------


                                                             startswith()

Utilizar :
La función startswith() se usa para verificar si una oración determinada comienza con una cadena en particular.
Los parámetros de inicio y fin son opcionales.
Podemos usarlos cuando queremos que solo se considere para la búsqueda alguna subcadena particular de la cadena 
original.

Devoluciones:
el valor devuelto es binario. 
Las funciones devuelven Verdadero si la oración original comienza con la cadena de búsqueda; de lo contrario, es False.
 
'''
# Ejemplo: True (Si la oración comienza con h)

cadena = "hola mundo".startswith('h')

print(cadena)

# Ejemplo: True (Si la oración comienza con hola)

cadena = "hola mundo".startswith('hola')

print(cadena)

# Ejemplo: False (Si la oración comienza con c)

cadena = "hola mundo".startswith('c')

print(cadena)


'''                                                          endswith()

El método endswith() devuelve True si una string termina con el sufijo dado; de lo contrario, devuelve False.

Sintaxis:

str.endswith (sufijo, inicio, fin)

Parámetros: 
    sufijo: el sufijo no es más que una string que debe comprobarse. 
    inicio: Posición inicial desde donde se necesita verificar el sufijo dentro de la string. 
    end: Posición final + 1 desde donde se necesita verificar el sufijo dentro de la string. 
    
Nota: Si no se proporciona el índice de inicio y finalización, por defecto toma 0 y la longitud -1 como índices de 
inicio y finalización donde el índice de finalización no está incluido en nuestra búsqueda. 

Devuelve: 
Devuelve True si la string termina con el sufijo dado; de lo contrario, devuelve False. 
'''
# Ejemplo: True (Si la oración termina con o)

cadena = "hola mundo".endswith('o')

print(cadena)

# Ejemplo: True (Si la oración termina con mundo)

cadena = "hola mundo".endswith('mundo')

print(cadena)

# Ejemplo: False (Si la oración termina con z)

cadena = "hola mundo".endswith('z')

print(cadena)


'''                                                          split()

split() convierte una cadena de texto en una lista. Por defecto, los elementos de dicha lista serán las palabras de 
la cadena.

sep representa el o los caracteres que deseamos utilizar como delimitador.

El método split(sep=None, maxsplit=-1) en Python devuelve una lista de palabras o tokens usando sep como cadena 
de separación. 
Básicamente, se utiliza para dividir o separar un string en partes.
'''
# Ejemplo: ['hola', 'mundo', 'mundo']

cadena = "hola mundo mundo".split()

print(cadena)

# Ejemplo: ['hola', 'mundo', 'mundo']

cadena = "hola-mundo-mundo".split('-') # Le indicamos que nos separe cuando haya un guion -

print(cadena)


'''                                                          join()

La función join() convierte una lista en una cadena formada por los elementos de la lista separados por comas. 
Los elementos se guardarán en la cadena, separados por el carácter que especifiquemos.
'''
# Ejemplo: n,a,h,u,e,l

cadena = ",".join("nahuel")

print(cadena)


'''                                                          strip()

Este método se utiliza para eliminar todos los espacios en blanco iniciales y finales de una cadena. 
También tiene en cuenta los tabuladores y saltos de línea. 
En realidad strip() devuelve una copia de la cadena con los caracteres iniciales y finales en blanco eliminados.
'''
# Ejemplo:

cadena = "     hola    ".strip()

print(cadena)

# Ejemplo: Elimina los espacios de (.)

cadena = ".....hola......".strip('.')

print(cadena)


'''                                                          replace()
Este método se utiliza para reemplazar datos en la cadena.

El método replace(sub, nuevo) de la clase string devuelve una copia del string con todas las ocurrencias del substring             
sub reemplazadas por el substring nuevo .
'''
# Ejemplo: "h0la mund0" quiero que reemplace todas las o por 0

cadena = "hola mundo".replace('o','0')

print(cadena)