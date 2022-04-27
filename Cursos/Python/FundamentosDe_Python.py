
    ========================================================================================================================================================================
	=                                                                        Curso de Python                                                                               =
    ========================================================================================================================================================================   

'''                                              ==============================  Hola Mundo  =================================    

.                                 ---------------------------------  Definición y uso La función print()  ----------------------------------

  imprime el mensaje especificado en la pantalla u otro dispositivo de salida estándar. El mensaje puede ser una cadena o cualquier otro objeto, el objeto se convertirá en una cadena 
  antes de escribirse en la pantalla. 
  Link: https://www.w3schools.com/python/ref_func_print.asp       
'''
  print("Hola mundo") 
  print("Mi nombre es Nahuel") 
# Se pueden usar comillas simples '' o dobles "".
# Si queremos hacer un salto de línea tenemos que poner \n (Alt Gr + ? = \).

print("Hola mundo\nmi nombre es Nahuel")   


'''                                    ==============================  Asignación De Valores | Varibles =================================                                                
    
    En Python existen 3 tipos de datos, (textos, númericos, booleanos)
    Vamos a usar una función para el ejemplo : 
    función type() en Python. 
    El método type() devuelve el tipo de clase del argumento (objeto) pasado como parámetro. La función type () se usa principalmente para fines de depuración. 
    Se pueden pasar dos tipos diferentes de argumentos a la función type(), uno y tres argumentos.

'''
# ----------------- Valores Númericos | Int ------------------ 
    número = 10
    print(número)

# ----------------- Valores Númericos con Decimales | Float ------------------ 
    numero = 20.5
    print(numero)


# ----------------- Cadenas de Textos | Str ------------------ 
    cadena = "Buenos días"

# Se pueden usar tanto comillas ("") como (''), e incluso COMBINARLAS
    cadena = "Estoy 'estudiando'"   # Esto va hacer que se muestre la palabra entre comillas


# ----------------- Valores Booleanos | Bool ------------------
# Para poder usarlo la primera letra debe comenzar con mayúscula
    valor = True
    valor = False

# ----------------- Operaciones con variables ------------------
    num1 = 10
    num2 = 6.2
    suma = num1+num2 * 10 / 6  # Aca dice: multiplicame el num2, el resultado dividilo por 6 y despues sumalo al num1
                               # esto se debe a las reglas de presedencia de python, si queremos que primero sume lo encerramos entra parentesis

num1 = 10
num2 = 6.2 
resultado = (num1+num2) * 10 / 6      # # Aca dice: suma el num1 + el num2 x 10 % 6

# Concatenación
print("El resultado es: ",resultado)


# ----------------- Tipado Dinamico ------------------
    valor = 10
    print(valor)

    valor = 'Nahuel'
    print(valor)


'''                                            ==============================  Operadores  =================================

.                                           ---------------------------------  Aritméticos  ----------------------------------          

    Los operadores Aritméticos permiten la realización de operaciones matematicas.

    Prioridad de los Operadores Aritméticos:
    1- Paréntesis () # es lo primero que se evalua de adentro a si afuera
    2- Exponenciación **
    3- Multiplicación, División y Módulo *, /, %
    4- Suma y Resta +, -
''' 
# ----------------- Suma ------------------
    num1 = 20
    num2 = 5
    resultado = num1 + num2
    print(resultado)         # Se puede hacer solo con el print pero para el ejemplo usamos variables

# ----------------- Resta ------------------
    num1 = 20
    num2 = 5
    resultado = num1 - num2
    print(resultado)

# ----------------- Multiplicación ------------------
    num1 = 20
    num2 = 5
    resultado = num1 * num2
    print(resultado)

# ----------------- División ------------------
    num1 = 20
    num2 = 5
    resultado = num1 / num2
    print(resultado)             # Esta división va a mostrar un resultado con decimales

# ----------------- División Entera ------------------
    num1 = 20
    num2 = 5
    resultado = num1 // num2 
    print(resultado)            # Esta división va a mostrar un resultado entero

# ----------------- División Entera ------------------
    num1 = 20
    num2 = 5
    resultado = num1 % num2
    print(resultado)            # Esto me va a mostrar el resto/residuo de la división

# ----------------- Exponenciación ------------------
    num1 = 2 
    num2 = 5
    resultado = num1 ** num2
    print(resultado)            # Esto me va a mostrar 2 elevado a la  quinta = 32



'''                                          ---------------------------------  Relacionales  ----------------------------------
    
    -Se utilizan para establecer una relación entre 2 valores.
    -Compara estos valores entre si y esta comparación produce un resultado de certeza o falsedad (Verdarero o Falso).
    -Tienen el mismo nivel de prioridad en su evaluación.
    -Los operadores relacionales tienen menor prioridad que los aritméticos.
    ¿Cuales son estos? :
    > | Mayor que
    < | Menor que
    >= | Mayor o igual que
    <= | Menor o igual que
    != | Diferente
    == | Igual
'''

#   /*------------ Mayor que -----------*/         /*------------ Menor que -------------*/    /*---------- Mayor o Igual que -------------*/
        resultado = 10 > 20                              resultado = 10 < 20                          resultado = 10 >= 20
        print(resultado)                                 print(resultado)                             print(resultado)

#    /*---------- Menor o Igual que -------------*/       /*---------- Diferente -------------*/     /*---------- Igual -------------*/
          resultado = 10 <= 20                                resultado = 10 != 20                       resultado = 10 == 20
          print(resultado)                                    print(resultado)                           print(resultado)



#                                       -----------------------  Combinando Operadores Aritméticos con Racionales  ----------------------

    a = 10
    b = 20
    c = 30
    resultado = a + b == c
    print(resultado)


'''                                        ---------------------------------  Operadores Lógicos  ----------------------------------

    -Permite construir expresiones lógicas, se obtiene como resultado "Booleanos".
    -Estos se deben poner en minusculas:
    And (Conjunción): and
    Or (Disyunción): or
    .     Negación: not

    Operador AND :
    Es una multiplicaión logica, ya que los dos valores tienen que ser positvos para que te arroje True.
    El operador AND lógico ( && ) devuelve true si ambos operandos son true y devuelven false de lo contrario. 
    Los operandos se convierten implícitamente al tipo bool antes de la evaluación y el resultado es de tipo bool .
    El operador AND lógico tiene asociatividad de izquierda a derecha.

    Operador OR :
    Se lo conoce como suma logica.
    Devuelve True si alguno de los operandos es True    

    Operador NOT :
    Devuelve True si alguno de los operandos False.
    Si tene un True y le asignas un Not te va a devolver False y viceversa

    -------------- Prioridad de los Operadores Lógicos --------------
        1. NOT
        2. AND
        3. OR

    -------------- Prioridad de los Operadores en General --------------
    1. ()
    2. **
    3. *, /, mod, not
    4. +, -, and
    5. >, <, ==, >=, <=, !=, or
'''

#  -------------- AND --------------
    a = 10
    b = 20
    c = 30
    resultado = ((b < a) and (c > b)) 
    print(resultado)                    # False


#  -------------- OR --------------
    a = 10
    b = 20
    c = 30
    resultado = ((b < a) or (c > b))
    print(resultado)                    # True    


#  -------------- NOT --------------
    a = 10
    b = 20
    c = 30
    resultado = not ((b < a) or (c > b))
    print(resultado)                    # False


'''                                     ---------------------------------  Operadores de Asignación  ----------------------------------
    Esto mas que nada nos va a ayudar a ahorrar codigo.
    Se utiliza un operador de asignación para asignar valores a una variable. 
    Esto generalmente se combina con otros operadores (como aritmética, bit a bit) donde la operación se realiza en los operandos y el resultado se asigna al operando izquierdo.

    OPERADOR                 DESCRIPCIÓN
        =          a = 5. El valor 5 es asignado a la variable a
        +=         a += 5 es equivalente a a = a + 5
        -=         a -= 5 es equivalente a a = a - 5
        *=         a *= 3 es equivalente a a = a * 3
        /=         a /= 3 es equivalente a a = a / 3
        %=         a %= 3 es equivalente a a = a % 3
        **=        a **= 3 es equivalente a a = a ** 3
        //=        a //= 3 es equivalente a a = a // 3
        &=         a &= 3 es equivalente a a = a & 3
        |=         a |= 3 es equivalente a a = a | 3
        ^=         a ^= 3 es equivalente a a = a ^ 3
        >>=        a >>= 3 es equivalente a a = a >> 3
        <<=        a <<= 3 es equivalente a a = a << 3
'''
# Ejemplo: supongamos que tenemos una variable y le queremos reasignar un dato/valor.

# -------- hasta ahora lo hariamoss asi: ----------
    a = 0
    a = a + 5
    print(a) 

# -------- Con Asignación ----------
    a = 0

    a  +=  5   # suma en asignación
    a  -=  2   # resta en asignación
    a  *=  3   # multiplicación en asignación
    a  /=  3   # división en asignación
    a  **= 2   # potencia en asignación
    a  %=  2   # modulo en asignación

    print(a)


'''                                           ---------------------------------  Salida de Datos  ----------------------------------

