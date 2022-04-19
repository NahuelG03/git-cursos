
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
.					                  ========================================================================================================                                       */
					
					
					
/*                                                  ==============================  Variables  =================================                                                     */

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

											
/*                                                                          Operadores lógicos	

	Los operadores lógicos se usan para combinar dos valores Booleanos y devolver un resultado verdadero, falso o nulo. Los operadores lógicos también se denominan operadores Booleanos.

	&& (y): Si los dos son verdaderos devuelve verdadero.
	|| (o): Basta con que uno sea verdadero para que devuelva verdadero.
	! (no): Negación

	Ejemplos:
*/			
	/*-------------------- && --------------------*/	                /*-------------------- || --------------------*/            /*-------------------- ! --------------------*/
		let resultado_V = true && true                                      let resultado_O = true || false || true 					let resultado_ = !false
		console.log(resultado_V)	                                        console.log(resultado_O)                                    console.log(resultado_)
	// esto nos da True                                                	// este nos da True                                         // este nos da True
		let resultado_F = true && false && true	                        // funciona a lo opuesto de && si hay un True               // va a hacer lo contrario a lo que le diga    
	// si hay un false dentro de la pregunta                            // en la pregunta va a devolver siempre True
	// va a devolver siempre False
	// Pero no es así con el O ||																																		 


/*                                            ==============================  Estructuras De Control  ==============================                                                  

	En lenguajes de programación, las estructuras de control permiten modificar el flujo de ejecución de las instrucciones de un programa.

	Condicionales:

	if/else (Si ocurre algo, haz esto, sino, haz lo esto otro...) if/else (si/no)
	?: operador ternario (Operador ternario: Equivalente a If/else , método abreviado.)
	switch (Estructura para casos específicos: Similar a varios If/else anidados.)
	Repetitivas o iterativas

	while
	do... while
	for
	
	Ejemplos:
*/
	if( condicion ) {
    // bloque verdadero
	}else {
  	// bloque falso
}

//	                                                                               Practicando			

// Ejemplo 1:

// Le decimos al usuario que escriba Javascript
	let stringUsuario = prompt('Escriba "JavaScript"')													

// Preguntamos si lo que escribio el usuario es correcto (Javascript)
	if(stringUsuario === 'JavaScript'){
		// en esta parte escribo lo positivo
	console.log('correcto')
	}
	else {
		// en esta parte escribo lo negativo
	console.log('incorrecto')
	}

// Ejemplo 2:

let numUsuario1 = prompt('Ingrese un número del 1 al 10')

if(numUsuario1 <= 10){
	console.log('perfecto!')
}
else {
	console.log('mal ahi´era del 1 al 10')
}

// Ejemplo 3:

let numUsuario = prompt("Ingrese numero del 1 al 10");

console.log(numUsuario + " Es: " + typeof numUsuario);

console.log(parseInt(numUsuario));

if (parseInt(numUsuario) <= 10) {
    // Sentencia true
    console.log("Genial!!");
} else {
    // Sentencia false
    console.log("Super mal!!");
}

/*                                                   ==============================  Swith  ==============================

	La declaración switch/Según evalúa una expresión, comparando el valor de esa expresión con una instancia case, y ejecuta declaraciones asociadas a ese case,
    así como las declaraciones en los case que siguen.
    Esta instrucción permite ejecutar opcionalmente varias acciones posibles, dependiendo del valor almacenado en una variable. Al ejecutarse, 
    se evalúa el contenido de la variable y se ejecuta la secuencia de instrucciones asociada con dicho valor.

	switch(opens new window)
	Plantillas literales (opens new window): Las plantillas literales son cadenas literales que habilitan el uso de expresiones incrustadas. Con ellas,
	es posible utilizar cadenas de caracteres de más de una línea, y funcionalidades de interpolación de cadenas de caracteres.
	Interpolación ( `` | Alt Gr + Ctrl )
	Ejemplos:
*/
	let opcionUsuario = prompt(`
	Elija una opción:
	1: Libros
	2: Películas
	3: Juegos
	`)
	console.log(opcionUsuario)
	// Swith
	switch(opcionUsuario){
		case '1':
			console.log('Martín Fierro')	  
		break
		case '2':
			console.log('John Wick')
		break
		case '3':
			console.log('Juega Counter Strike')
		break
		default:
			console.log('Opción no valida')
		break
	}

/*                                                    ==============================  While  ==============================

	While/Mientas Crea un bucle que ejecuta una sentencia especificada mientras cierta condición se evalúe como verdadera. Dicha condición es evaluada antes de ejecutar la sentencia.

	Increment (++): El operador de incremento (++) incrementa (suma uno a) su operando y devuelve un valor.
	Si se usa postfijo, con operador después del operando (por ejemplo, x++), el operador de incremento incrementa y devuelve el valor antes de incrementar.
	Si se usa como prefijo, con el operador antes del operando (por ejemplo, ++x), el operador de incremento incrementa y devuelve el valor después del incremento.
	link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment

	Ejemplos:
*/
	let numero = 1

	while (numero <= 10) {
		console.log(numero)
		numero ++ // numero = numero + 1
	}
	console.log("fin numero " + numero)


/*                                                                               Juego De Adivinar

Math.random(): La función Math.random() retorna un punto flotante, un número pseudo-aleatorio dentro del rango [0, 1).
Esto es, desde el 0 (Incluido) hasta el 1 pero sin incluirlo (excluido), el cual se puede escalar hasta el rango deseado.
La implementación selecciona la semilla inicial hasta el algoritmo que genera el número aleatorio; este no puede ser elegido o cambiado por el usuario.

link: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math/random
Ejemplos:
*/
	// Retorna un número aleatorio entre 0 (incluido) y 1 (excluido)
	function getRandom() {
  	 return Math.random();
	}
	// Retorna un número aleatorio entre min (incluido) y max (excluido)
	function getRandomArbitrary(min, max) {
  	 return Math.random() * (max - min) + min;
	}

	// Retorna un entero aleatorio entre min (incluido) y max (excluido)
	// ¡Usando Math.round() te dará una distribución no-uniforme!
	function getRandomInt(min, max) {
	  return Math.floor(Math.random() * (max - min)) + min
	}

	//                                                                                  Juego

	let numeroMaquina = Math.floor(Math.random() * (10 - 1)) + 1

	let vidas = 3
	 let numeroUsuario = parseInt(prompt("Adivine el número del 1 al 10"))

	while(numeroMaquina !== numeroUsuario && vidas > 1) {

		let mensaje = (numeroMaquina > numeroUsuario) ? 'El número Maquina es mayor' : 'El número Maquina es menor'  //true : false // operador ternario

		console.log('Te equivocaste!' + mensaje)
		numeroUsuario = parseInt(prompt("número del 1 al 10"))
		vidas --
	}

	if (numeroMaquina === numeroUsuario) {
		console.log('Ganaste')
	} 
	else {
		console.log('Perdiste')
	}


/*                                                     ==============================  Array  ==============================

	Los Arrays/Arreglos son objetos similares a una lista cuyo prototipo proporciona métodos para efectuar operaciones de recorrido y de mutación.
	Tanto la longitud como el tipo de los elementos de un array son variables.
	Los arrays se identifican con los corchetes [] ( Ctrl + Mayús + tecla q contiene { ).
	
	Conceptos claves:
	length: Tamaño de array (cantidad de elementos)
	índice: Comienzan en cero, es decir, el índice del primer elemento de un array es 0.
	undefined: Una variable a la que no se le ha asignado valor, o no se ha declarado en absoluto (no se declara, no existe) son de tipo undefined. 
	Un método o sentencia también devuelve undefined si la variable que se está evaluando no tiene asignado un valor. Una función devuelve undefined si no se ha devuelto un valor.

	Ejemplos:
*/
	// Lista De Frutas
	let frutas = ['banana', 'manzana', 'naranja']
	console.log(frutas)
	console.log(frutas.length)
	// Pintando un producto en la consola
	console.log(frutas[1]) // esta es la Manzana


/*                                                        ==============================  For  ==============================

	La instrucción For/Para ejecuta una secuencia de instrucciones un número determinado de veces.
	For crea un bucle/loop que consiste en tres expresiones opcionales, encerradas en paréntesis y separadas por puntos y comas, seguidas de una sentencia ejecutada en un bucle.
	links: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/for
	Ejemplos:
*/
	let frutas2 = ["pera", "kiwi", "mandarina"]

	for (let i = 0; i < frutas2.length; i ++) {
		console.log(frutas2[i])
	}

/*                                                                                       For Of

	La sentencia sentencia for...of ejecuta un bloque de código para cada elemento de un objeto iterable, como lo son: String, Array, 
	objetos similares a array (por ejemplo, arguments or NodeList), TypedArray, Map, Set e iterables definidos por el usuario.
	La sintaxis de for...of es específica para las colecciones, y no para todos los objetos. 
	Esta Iterará sobre cualquiera de los elementos de una colección que tengan la propiedad [Symbol.iterator].
	Ejemplos:
*/
	let frutasOf = ('uva', 'piña', 'damasco')
	for (let fruta of frutasOf) {
		console.log(fruta)
	}

/*                                                                                        For In
	El bucle for...in iterará sobre todas las propiedades de un objeto. Más tecnicamente, iterará sobre cualquier propiedad en el objeto que haya sido internamente definida con
	su propiedad [[Enumerable]] configurada como true.
	Ejemplo:
*/
	for (let fruta in frutas) {
    console.log(fruta);
	}


/*                                                       ==============================  Function  ==============================                      

   Las funciones son uno de los bloques de construcción fundamentales en JavaScript. 
   Una función en JavaScript es similar a un procedimiento — un conjunto de instrucciones que realiza una tarea o calcula un valor, pero para que un procedimiento califique como
   función, debe tomar alguna entrada y devolver una salida donde hay alguna relación obvia entre la entrada y la salida.
   Características:
	El nombre de la función.
	Una lista de parámetros de la función, entre paréntesis y separados por comas.
	Las declaraciones de JavaScript que definen la función, encerradas entre llaves, { ... }.
	links: https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Functions

	HOISTING: una estricta definición de hoisting sugiere que las declaraciones de variables y funciones son físicamente movidas al comienzo del código, 
	pero esto no es lo que ocurre en realidad. Lo que sucede es que las declaraciones de variables y funciones son asignadas en memoria durante la fase de compilación, 
	pero quedan exactamente en dónde las has escrito en el código.

	Conclusión: Es como que javascript hace un barrido sin ejecutar nada, pero en la memoria Ram que tiene cuando escribimos este lee todo nuestro código haciendo tipo un barrido
	pero lee solo la función no lo que esta dentro y luego empieza a meter todo en la memoria y despues ya sabe que la función empieza arriba, por eso si la llamamos el ya la va
	a leer y recien ahí va a entrar en su interior.

	Ojito!!
	"Hoisting" usualmente es una pregunta técnica en una entrevista de trabajo 😲

	Ejemplos:
*/

	function saludar () {
		console.log('Bienvenido! ')
	}
	saludar()

	// Concatenación
	function saludar(nombreUsuario) {
		return "Bienvenido! " + nombreUsuario
	}
	console.log(saludar("Nahuel"))

	// Ejercicio Suma     
	function sumar (n1, n2) {
		return parseInt(n1) + parseInt(n2)
	}
	let numUno = prompt("Ingrese primer numero")
	let numDos = prompt("Ingrese segundo numero")

	consolo.log(sumar(numUno, numDos))




	========================================================================================================================================================================
    =                                                                          Conceptos Claves                                                                            =
    ========================================================================================================================================================================



 /*=====                                                                   interpolación template string                                                                        ======

	Las plantillas literales son cadenas literales que habilitan el uso de expresiones incrustadas. Con ellas, es posible utilizar cadenas de caracteres de más de una línea, 
	y funcionalidades de interpolación de cadenas de caracteres.

	template string Link: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Template_literals
	Las plantillas de cadena de caracteres pueden contener marcadores, identificados por el signo de dólar y envueltos en llaves ${expresión}. 
	Las expresiones contenidas en los marcadores, junto con el texto

	Interpolación de expresiones:
	-barra invertida "alt Gr + ?"  
	-acento grave "alt + 96"

	Ejemplo:
*/
	// --------------- Interpolación de expresiones ----------------
 		let nombreUsuario = "Nahuel"
 		console.log('\nBienvenido: \n' + nombreUsuario + '\n') 


/* 		con las plantillas literales, se pueden utilizar sus nuevas capacidades 
 		(es decir, insertar expresiones con ${ } e incluir caracteres de fin de linea literales dentro de la cadena) para simplificar la sintaxis:
*/
 		let nombreMascota = 'Shara'
 		console.log(`El nombre de su mascota es: 
 			${nombreMascota} // con esto llamamos a la variable 
 		 `)

 	// ------------------------ Métodos --------------------------
 		let nombreUsuario = 'Nahuel'
 		console.log('Bienvenido: ${nombreUsuario.toUpperCase()}')


 	// -------------------- Operador Ternario --------------------
 		let nombreUsuario = 'Nahuel'
 		let estado = false  

 		console.log(`
 		${estado ? 'Bienvendo!' : 'Adiós!'}	${nombreUsuario}
 		 `) 


/*                                        =================================  VAR vs LET vs CONST  =====================================


/*                                               ---------------------------------  VAR  ----------------------------------                                                           
	
	Uno de los mayores problemas al declarar variables con VAR, es que puede sobrescribir las declaraciones de variables sin errores.
	
	Ejemplo:
*/
		var nombreGato = Mishi   
		var nombreGato = fuzz 
		console.log(estado)   // esto siempre va a dar el segundo valor que le asignemos en este caso Fuzz
/*
	En una aplicación pequeña, es posible que no se encuentre con este tipo de problema, pero cuando su código se agrande, 
	puede sobrescribir accidentalmente una variable que no tenía la intención de sobrescribir.

	Debido a que este comportamiento no arroja un error, la búsqueda y corrección de errores se vuelve más difícil. 
	Se introdujo let una nueva palabra clave llamada en ES6 para resolver este problema potencial con var.
*/


/* 													---------------------------------  Scope  ----------------------------------

	Siguiendo con el tema de las variables en Javascript, conozcamos el scope.

	TIP: En simples palabras el "scope de una variable" hace referencia al lugar donde esta va a vivir o podrá ser accesible.

	Cuando declaras una variable con VAR, se declara globalmente o localmente si se declara dentro de una función.
*/		
		var estado = true
		if (estado) {
    		var estado = false
		}
		console.log(estado)



/*                                                ---------------------------------  LET  ----------------------------------

	let: Una variable con el mismo nombre solo se puede declarar una vez.
*/
		let userName = 'Jorge'
		let userName = 'Messi'
		console.log(userName)

//  Pero si se puede cambiar su valor:
	
		let userName = 'Jorge'
		userName = 'Messi'
		console.log(userName)

/*
	let se comporta de manera similar, pero con algunas características adicionales. Cuando declaras una variable con let dentro de un bloque, declaración o expresión, 
	su alcance se limita a ese bloque, declaración o expresión.
*/

		let estado = true
		if (estado) {
		    let estado = false
		    console.log(estado)
		}
		console.log(estado)	
	


		for (let i = 0; i < 10; i++) {
	    	console.log(i)
		}
		console.log(i)


/* 													---------------------------------  CONST ----------------------------------

	const tiene todas las características increíbles de let, con la ventaja adicional de que las variables declaradas usando const son de solo lectura. 
	Son un valor constante, lo que significa que una vez que se asigna una variable const, no se puede reasignar.

	Algunos desarrolladores prefieren asignar todas sus variables usando const de forma predeterminada, a menos que sepan que necesitarán reasignar el valor. 
	Solo en ese caso, usan let.
*/											

//   ------------- Error 1 ---------------
		const estado = true										
		estado = false

//   ------------- Error 2 ---------------						// estos errores solo funcionan con LET								
		for (const i = 0; i < 10; i++) {
			console.log(i)
		}

//   ------------- Válido -----------------
		const estado = true
		if (estado) {
			const estado = false
			console.log(estado)
		} 
		console.log(estado)


/* 											 ====================================  Array Vs Const  =====================================							

	Es importante comprender que los objetos (incluidos los arreglos y las funciones) asignados a una variable mediante el uso const siguen siendo mutables. 
	El uso de const solo evita la reasignación del identificador de variable.
*/

//  -------------- Error --------------
		const miArray = []
		miArray = ["nuevoElemento"]

//  ------------- Válido ---------------	
		const miArray = []
		miArray[0] = ["nuevoElemento"]
		console.log(miArray)


/* 										---------------------------------  Array (push, pop, shift, unshift) ----------------------------------
	

.											      --------------------------------- Push/Empujar ----------------------------------
														
	El método push() añade uno o más elementos al final de un array y devuelve la nueva longitud del array.
*/
		const frutas = ['sandía', 'pera']

		frutas.push('banana')  // esto va a agregar la "banana" al final de la lista

		console.log(frutas)

/*

.                                                   --------------------------------- Unshift ----------------------------------            

	El método unshift() agrega uno o más elementos al inicio del array, y devuelve la nueva longitud del array.
*/
	const frutas = ['sandía', 'banana']

	frutas.unshift('pera') // esto va a agregar la "pera" al pricipio de la lista

	console.log(frutas)


/*                                                    --------------------------------- Pop ----------------------------------

	El método pop() elimina el último elemento de un array y lo devuelve. Este método cambia la longitud del array.
*/

	const frutas = ['sandía', 'pera']

	frutas.pop()   // con esto le digo que elimine el ultimo elemento de la lista

	console.log(frutas)

// para devolver el ultimo elemento tendremos que crear una constante, sería como una variable Auxiliar
	
	const frutas = ['sandía', 'pera']

	const frutaEliminada = frutas.pop()

	console.log(frutas)
	console.log(frutaEliminada)


/* 												     --------------------------------- Shift ----------------------------------				

	El método shift() elimina el primer elemento del array y lo retorna. Este método modifica la longitud del array.
*/
	const frutas = ['sandía', 'pera']

	const frutaEliminada = frutas.shift()      // este solo va a eliminar el primer elemento de la lista

	console.log(frutas)
	console.log(frutaEliminada)


/* 												======================================  Confirm =====================================		

	El método Window.confirm() muestra una ventana de diálogo con un mensaje opcional y dos botones, Aceptar y Cancelar.

	Message: es la cadena que se muestra opcionalmente en el diálogo.
	Result: es un valor booleano indicando si se ha pulsado Aceptar o Cancelar (Aceptar devuelve true).
*/
//         Sintaxis
	result = window.confirm(message);

//                    Ejemplo
	if (window.confirm("Do you really want to leave?")) {
	  window.open("exit.html", "Thanks for Visiting!");
	}



/*	                                                                           Práctica: carrito de compras
	El objetivo es crear una aplicación que nos permita ir agregando elementos a un carrito de compras: ver ejemplo(opens new window)
	confirm(): muestra una ventana de diálogo con un mensaje opcional y dos botones, Aceptar (true) y Cancelar (false).
*/
	const frutas = []
	const fruta = prompt('🍒 Feria Market 🍉 ¿qué fruta desea comprar?')

	frutas.push(fruta)

	while (confirm('¿Desea agregar otro elemento al 🛒?')) {
	    const fruta = prompt('¿qué fruta desea comprar?')
	    frutas.push(fruta)
	}

	console.log('Ustede compró: ')
	for (let fruta of frutas) {
	    console.log(fruta)
	}


/* 										 	======================================  Funciones Anónimas =====================================					
						
	En JavaScript, usualmente no necesitas nombrar tus funciones, especialmente cuando se pasa una función como argumento a otra función. En su lugar, 
	creamos funciones inline (en línea). No necesitamos nombrar estas funciones porque no las reutilizamos en otro lugar.

	TIP:
	La forma correcta de definir una función varía según el comportamiento que esperemos de la misma: con las funciones declaradas, tenemos la seguridad de que siempre estarán 
	disponibles en tiempo de ejecución. Con las funciones Expresadas, tendremos que éstas no son evaluadas hasta que el intérprete no alcance su posición en el código, 
	lo cual puede generar errores en arquitecturas muy anidadas.

	El hecho de que las funciones Declarativas se evalúen antes que las expresiones, pueden producir comportamientos no deseados cuando forman parte de condicionales.
	Para estos casos, el uso de las funciones expresadas garantiza que éstas formarán parte del flujo general del programa, lo cual puede evitarnos sorpresa en determinados 
	entornos.
	Link: https://www.etnassoft.com/2011/09/02/funciones-declaradas-vs-funciones-expresadas-en-javascript/

	ES6 nos proporciona el azúcar sintáctico, para no tener que escribir funciones anónimas de este modo. En su lugar, puedes usar la sintaxis de función flecha (Arrow).

	Arrow functions: Una expresión de función flecha es una alternativa compacta a una expresión de función tradicional

	Limitantes:
	No tiene sus propios enlaces a this o super y no se debe usar como métodos.
	No tiene argumentos o palabras clave new.target.
	No apta para los métodos call, apply y bind, que generalmente se basan en establecer un ámbito o alcance
	No se puede utilizar como constructor.

	Link: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Functions/Arrow_functions
*/

//  ------------------ Función Declarativa ----------------------
	// declaro la función
	function numAleatorioRango(min, max) {
    	return Math.floor(Math.random() * (max - min)) + min;
	}

	// invoco la función
	console.log(numAleatorioRango(1, 11))

// --------------------- Función Expresada -----------------------
	const numAzar = function(min, max) {
		return Math.floor(Math.random() * (max - min)) + min
	}
	console.log(numAzar(100, 201))

// --------------------- Funciónes Flecha -----------------------
	const azarFlecha = (min, max) => {
		return Math.floor(Math.random() * (max - min)) + min
	}
	console.log(azarFlecha(1, 11))


//                       Cualidades
	const miNumeroFlecha = (max) => {
    	return Math.floor(Math.random() * (max - 1)) + 1;
	}

	console.log(miNumeroFlecha(11))


//	                     Reducción:
	const miNumeroFlecha = max => Math.floor(Math.random() * (max - 1)) + 1;
        
	console.log(miNumeroFlecha(11))

//	            Reducción con paréntesis:
	const miNumeroFlecha = max => (Math.floor(Math.random() * (max - 1)) + 1);
	        
	console.log(miNumeroFlecha(11))

//	                Más parámetros:
	const miNumeroFlecha = (min, max) => Math.floor(Math.random() * (max - min)) + min;

	console.log(miNumeroFlecha(1, 11))

//	Parámetros opcionales (también se puede hacer con function):
	const miNumeroFlecha = (min = 1, max = 10) => Math.floor(Math.random() * (max - min)) + min;

	console.log(miNumeroFlecha())



/*                                     ======================================  Arrow & forEach() =====================================

	forEach(): El método forEach() ejecuta la función indicada una vez por cada elemento del array.

	Parámetros:
	callback
	Función a ejecutar por cada elemento, que recibe tres argumentos:
	currentValue
	El elemento actual siendo procesado en el array.
	index Opcional
	El índice del elemento actual siendo procesado en el array.
	array Opcional
	El vector en el que forEach() esta siendo aplicado.
	thisArg Opcional
	Valor que se usará como this cuando se ejecute el callback.

	Valor de retorno: undefined.

	Link: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach

	Ejemplos:
*/
	let frutas = ['manzana', 'sandía', 'naranja']
	frutas.forEach((fruta, index, array) => {
		console.log(index)
		console.log(fruta)
		console.log(array)
	})

//	En nuestro ejemplo de carrito de compras:

	const carrito = []
	const fruta = prompt('🍒 Feria Market 🍉 ¿qué fruta desea comprar?')

	carrito.push(fruta)

	while (confirm('¿Desea agregar otro elemento al 🛒?')) {
	    const fruta = prompt('¿qué fruta desea comprar?')
	    carrito.push(fruta)
	}

	console.log('Ustede compró: ')
	carrito.forEach((fruta, index) => (
	    console.log(`${index + 1}: ${fruta}`)
	))




	========================================================================================================================================================================
    =                                                                         Objetos                                                                            =
    ========================================================================================================================================================================

/*
	JavaScript está diseñado en un paradigma simple basado en objetos.
	Un objeto es una colección de propiedades, y una propiedad es una asociación entre un nombre (o clave) y un valor.
	El valor de una propiedad puede ser una función, en cuyo caso la propiedad es conocida como un método.
	Además de los objetos que están predefinidos en el navegador, puedes definir tus propios objetos.
	Los objetos son similares a los arreglos (arrays), excepto que en lugar de usar índices para acceder y modificar sus datos, accedes a los datos en objetos a través de 
	propiedades (properties).

	Link: https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Working_with_Objects
*/


/*                                  ======================================  Objeto Literal =====================================

	Se denomina objeto literal al objeto cuyas propiedades están declaradas textualmente en el código.
	Link: https://dev.to/duxtech/es6-objetos-literales-en-javascript-58np
*/
		const mascota = {
		  nombre: 'Shara', 
		  edad: 4,
		  duerme: true,
		  enemigos: ['perros, gatos']
		}


//     Acceder a los valores
//    Notación de punto:

console.log(gato.nombre)
console.log(gato.duerme)
console.log(gato.enemigos[0]);

//  Notación de corchetes (nos servirá para recorrerlo):

console.log(gato['nombre'])
console.log(gato['edad'])
console.log(gato["enemigos"][0]);


//  						    	======================================  CRUD (Propiedades) =====================================

//   Crear (create)
	gato.color = 'Azul'

//	  Leer (read)
	console.log(gato)

//  Actualizar (update)
	gato.edad = 11

//  Eliminar (delete)
	delete gato.duerme	



/* 								  ======================================  hasOwnProperty =====================================			

	A veces es útil comprobar si existe o no la propiedad de un objeto dado. Podemos utilizar el método .hasOwnProperty(propname) para determinar si un objeto tiene una 
	propiedad con ese nombre. .hasOwnProperty() devuelve true o false si se encuentra la propiedad o no.
*/

	const mascota = {
		nombre: 'Shara',
		duerme: true,
    	edad: 4,
    	enemigos: ["perros", "gatos"]
	}

	console.log(gato.hasOwnProperty("nombre"))
	console.log(gato.hasOwnProperty("salud"))


/*                              ======================================  Objetos Anidados =====================================                                              */

	const mascota = {
		nombre: 'shara',
		duerme: true,
		edad: 4,
		enemigos: ["perros", "gatos"]
		otros: {                                // Apartir de aca empiezan los obejetos anidados
			amigos: "mishi", "misha"
			favoritos: {
				comida: {
					fria: "huesos",
					caliente: "asado"
				}
			}
		} 
	}

	console.log(mascota.otros.amigos[0])
	console.log(mascota.otros.favoritos.comida.caliente)
	


/* 								======================================  Encadenamiento Opcional =====================================

	Optional chaining: El operador de encadenamiento opcional ?. 
	permite leer el valor de una propiedad ubicada dentro de una cadena de objetos conectados sin tener que validar expresamente que cada referencia en la cadena sea válida.

	Link: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/Optional_chaining
*/
