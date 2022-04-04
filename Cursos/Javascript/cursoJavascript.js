
========================================================================================================================================================================
=                                                                  Curso de JavaScript                                                                                 =
========================================================================================================================================================================

/*
    JavaScript distingue las minisculas de las mayusculas por lo que arbol no es lo mismo que Arbol o casa no es lo mismo que Casa, ademas interpreta el idioma 
    ingles, por lo que si pones caracteres que en un teclado de ingles no figuran como la Ñ, te va a saltar un error.

    TIP-Emojis: para hacer emojis presionamos la tecla de (Windows + .), o tambien copiar un emoji de una página.
 */


/*----------------------------------------------       ¿Como vincular un documento de Javascript con el html?      ----------------------------------------------------*/
/*  
 	Una forma de vincularlo es: en el Tag Head del html le ponemos un tag <script></script>. 
 	2: Lo mismo pero en la etiqueta Body. 
 	3: La forma correcta es usarlo con la propriedad src Ej: <script src="Link del archivo Js"></script>.
*/

/*--------------------------------------------------------------------  Palabras Reservadas  --------------------------------------------------------------------------*/
/*
 	Las palabras reservadas son aquellas que cada lenguaje se guarda para su uso funcional, es decir, 
 	palabras que tienen un significado y una función específica dentro del lenguaje. Por lo cual, debemos tener cuidado en no utilizar dichas palabras reservadas. 
 	Usar las palabras claves es mala practica porque perjudica el SEO del sitio web.

 	¿Cuál es la función de palabras reservadas?
    En los lenguajes informáticos, una palabra reservada es una palabra que tiene un significado gramatical especial para ese lenguaje y no puede ser utilizada como
    un identificador de objetos en códigos del mismo, como pueden ser las variables.

 	link: ( https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Lexical_grammar#palabras_clave)
 */
 // Ejemplo:
  alert("esto es una alerta del navegador string es un texto")

  /*--------------------------------------------------------------------  Orden De Ejecución  -------------------------------------------------------------------------*/
  
/*
	Cuando el navegador encuentra un bloque de JavaScript, generalmente lo ejecuta en orden, de arriba a abajo. 
	Esto significa que debes tener cuidado con el orden en el que colocas las cosas.
	Ejemplo: 
 */	 
	alert("primero");
	alert("segundo");
	alert("tercero");

/*----------------------------------------------------------------------------  Consola  ------------------------------------------------------------------------------*/
/*
	Si abrimos el inspector de elementos, podrás ver una pestaña de consola.

	La consola del navegador es una herramienta que nos ayuda a depurar nuestras páginas, facilitando nuestro trabajo diario.
	Esta es una función/acción que recibe parametros.

	Ejemplo:
*/

	console.log("esto es la consola")
	
/*--------------------------------------------------------------------------- Tipo De Datos  --------------------------------------------------------------------------*/
/*
 	Como practicamos,  los textos que enviamos a la consola van entre comillas "text" o 'texto' .
 	Esto pasa porque existen distintos tipos de datos en javascript

 	El último estándar ECMAScript define nueve tipos (opens new window), pero por ahora nos centraremos en 3.
 	ECMAScript es una especificación de lenguaje de programación publicada por ECMA International.

 	Este determina cómo emplear el lenguaje Javascript, que permite a los fabricantes de software desarrollar las herramientas adecuada para interpretarlo correctamente.

	Links: (ECMA) https://developer.mozilla.org/es/docs/Web/JavaScript/Data_structures
		   (es6) http://kangax.github.io/compat-table/es6/

	Datos:
	1- String: se utiliza para representar datos textuales.
	   Se puede cerrar con "" o '', incluso usar algunas de esta para destacar algo, en el Ej el destacado es 'es' .

	2- Number: valores numéricos.
	   Se pueden usar todos los valores,  enteros, decimales, negativos etc, pero si queremos separan dos números usamos una , como en el Ej.

	3- Boolean: representa una entidad lógica y puede tener dos valores: true y false.

	Ejemplos:
*/	
	 /*------------- Valor String ----------------*/

        console.log('tambien "es" un string')
	
	/*-------------- Valor Number ----------------*/

		console.log(20)
		console.log(20.6)
		console.log(20, 30)
		console.log(1 + 1)

	/*-------------- Valor Boolean ---------------*/  
		console.log(true)
		console.log(false)


					                           
/*                                    ========================================================================================================
.					                           =                            Fundamentos De Programación                          =
.					                  ========================================================================================================                                                   */
					
					
					
 /*                                                 ==============================  Variables  =================================                                                     */

/*
    	¿Qué son las variables?: Es un espacio de memoria que yo género/reservo para guardar un dato.
    	Pasos: 1- Generamos ele espacio de memoria
    		   2- Pornerle un nombre
    		   3- Cargarle un dato

    	JavaScript tiene 3 tipos de declaraciones d variables
    	1- Var
    	2- Let
    	3- Const
*/					                             
/*                                                                                   Variable Let                                                                                     */		

/* Para declarar/crearla usamos Let + El nombre + = + El valor

	Reglas para el nombre de sus variables:
	No utilizar espacios, en su lugar reemplazar con _ o camelCase (opens new window)
	Utilizar lengua inglesa, sin ñ ni tildes (en teoría se puede pero es una mala práctica)
	Evitar signos extraños como @#][+{}- etc.
	El primer carácter no puede ser un número var 2res = 'algo'
	Se puede utilizar el signo $ ej: var $anio = 2021. 
	Utilizar nombres descriptivos

	(En JS el signo = se conoce como Operador de asignación simple)
	El signo = en Javascript se conoce como asignación (permite almacenar un valor a una variable).
	Se evalúa la expresión de la derecha y luego se le asigna el resultado a la variable de la izquierda.
	A esto se le llama declarar la variable con un valor inicial.

	Ejemplos:
*/
	let nombreUsuario = "Ignacio"
	let edadUsuario = 33
// Para "pintarlos" que se muestre en la consola deñ navegador usamos console.log
	console.log(nombreUsuario)
	console.log(edadUsuario)




 /*                                                =============================  Concatenación  ===============================                                                      */
 /*
 	Nos sirve para unir una o más variables, también lo puedes mezclar con diferentes tipos de datos.
 	Concatenar es una elegante palabra de la programación que significa: "unir". Para unir cadenas en JavaScript el símbolo de más +, el mismo operador que usamos para sumar números,
  	pero en este contexto hace algo diferente. Vamos a probar un ejemplo en nuestra consola.
  */ 
  	let nombreMascota = "Shara"
  	let edadMascota = 4
  	console.log("el nombre de tu mascota es: " + nombreMascota + " " + edadMascota) // El + " " + es un espacio en blanco
 	console.log("mi nombre es: " + "Ignacio") // No hace falta la varaiable ya que la concatenamos "Ignacio"

// Aquí se ejecutará la operación aritmética, pero recuerda que si puedes concatenar un número y un string.
 	var numeroUno = 100;
	var numeroDos = 200;
	console.log(numeroUno + numeroDos); 

 /*                                          ======================================  Prompt  =====================================                                                    */
//Para hacer nuestro ejemplos más dinámicos conozcamos prompt. Es una palabra reservada.
// Ejemplos:
	prompt("ingresa un apellido") // Si lo dejamos haci cuando ingrese su apellido se va a perder, para poder guardarlo lo vamos a poner en una variable.
	let apellido = prompt("ingresa un apellido")
	console.log(apellido)

	let numeroUno = prompt("Ingresa el primero número");
	let numeroDos = prompt("Ingresa el segundo número");
	let resultado = numeroUno + numeroDos;
	console.log(resultado); // ¿no es el resultado esperado?

/*                                                                                    Typeof                                                                                          */
/*
	El operador typeof se usa en cualquiera de los siguientes modos:

	1- typeof operando
	2- typeof (operando)
	El operador typeof devuelve una cadena que indica el tipo del operando sin evaluarlo. operando es la cadena, variable, palabra clave u objeto para el que se devolverá su tipo. 
	Los paréntesis son opcionales.
	Link: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/typeof
*/

/*                                                                                   Parseint                                                                                         */	
/*
	Convierte (parsea) un argumento de tipo cadena y devuelve un entero de la base especificada. 
	link: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/parseInt#resumen
	Ejemplo:
*/
	console.log(parseInt(numeroUno))
	let resultado = parseInt(numeroUno) + parseInt(numeroDos)


/*                                             =================================  Operadores  =================================                                                       */
	
/*
	Existen diferentes tipos de operadores:

	.Operadores Aritméticos o Algebraicos o Matemáticos.
	.Operadores de Comparación / Relacionales.
	.Operadores lógicos.

.                                                                           Operadores Aritméticos   

	En programación y matemáticas, los operadores aritméticos son aquellos que manipulan los datos de tipo numérico, es decir,
 	permiten la realización de operaciones matemáticas (sumas, restas, multiplicaciones, etc.)
	Ejemplos:
*/
	/*---------------- Suma ---------------*/      	/*------------------- Resta -----------------*/       /*--------------- Multiplicación --------------*/  
		let resultadoSuma = 10 + 20 					let resultadoResta = 10 - 20                          	let resultadoMulti = 10 * 20
		console.log(resultadoSuma)						console.log(resultadoResta)                             console.log(resultadoMulti)

		let resultadoDecimal = 10.5 + 20				let resultadoResta_decimal = 10.5 - 20					let resultadoMulti_decimal = 10.5 * 20
		console.log(resultadoDecimal)					console.log(resultadoResta_decimal)	                    console.log(resultadoMulti_decimal)


	/*--------------- División ------------*/	   /*------------------ Sobrante ----------------*/	       /*------------------ Jugando ------------------*/
		let resultadoDivisión = 20 / 10                let resultadoSobrante = 20 % 12							let resultado = (2 * (100 / 5) + 10)
		console.log(resultadoDivisión)                 console.log(resultadoSobrante)							console.log(resultado)

								
/*
.																		   Operadores Relacionales

	Los operadores relacionales definidos por JavaScript son idénticos a los que definen las matemáticas: mayor que (>), menor que (<), mayor o igual (>=),
	menor o igual (<=), igual que (===) y distinto de (!==).
	Esto nos va a mostrar si es Verdadero/True o si es Falso/False.
	Ejemplos:
*/
	/*------------- Mayor qué ------------*/	   /*--------------- Menor qué -----------------*/			/*---------------- Igual qué ---------------*/													
		let resultado = 10 > 20                        let resultadoMenor = 20 < 10                              let resultadoIgual = 10 === 20
		console.log(resultado) 	                       console.log(resultadoMenor)								 console.log(resultadoIgual)

	/*--------------- Diferente -----------------*/
		let resultadoDiferente = 10 !== 20		
		console.log(resultadoDiferente)				

																																		 