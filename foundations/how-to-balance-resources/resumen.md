# How to balance resources - the pragmatic programmer (20 aniversario)

> "Si encendemos lugar, damos lugar a la aparición de una sombra", frase que acompaña a la intro del episodio.

En este capítulo el autor se propone a hablar sobre el manejo de recursos dentro de un programa. Trae a la conversación 
la idea básica que podemos tener nosotros sobre lo que es un recurso en el mundo de la programación: un programa en si, 
un objeto, un archivo que abrimos y usamos, un actor externo que invocamos, etc. Se menciona que el patrón clásico para 
el manejo de recursos es: abrirlo, operar sobre él y luego cerrarlo. 

**El problema** es que no muchos programadores saben como lidiar correctamente con los recursos, sin embargo 
el capítulo introduce en este punto una frase muy precisa: **termina lo que empiezas.**

Dentro de la misma introducción pone un ejemplo de un programa que representa un mal manejo de recursos, 
consiste en lo siguiente: 

* Tenemos una función de lectura que introduce el archivo hacia el programa y lo deja como variable
* Tenemos una función de escritura que escribe la variable creada previamente hacia el disco y luego cierra la conexión con el archivo original
* Una función de actualización que usa ambas funciones anteriores pero que en el medio hace cierto cálculo.

El problema es que quién usa al archivo realmente es la función de actualización, apoyada en las dos definidas previamente, sin embargo
en el cuerpo de esa función nunca vemos que el recurso se libere explicitamente: **es algo que le corresponde a la función de escritura.**
Esto está mal porque desde la función que lee el archivo tenemos una variable compartida y eso hace que las funciones de lectura y escrituda
estén acopladas entre sí, eso lleva a que **potencialmente introduzcamos un bug dentro del código** a la hora de tener que modificar la lógica 
de actualización.

**La solución** propuesta por el autor (o autores, son 2 si no me equivoco, je) es que las funciones de lectura y escritura
no contengan una referencia a la variable que representa al archivo leido sino que la reciban como argumento. Eso hace que la función
de actualización tenga toda la carga de leer el archivo y luego volverlo a cerrar, además de usar los otros dos métodos renovados.

De ese modo cumplimos con que la función de actualización **termine lo que empieza.**

Luego sobre el final de esta introducción el autor menciona que muchos lenguajes modernos (en python pasa) existe esto de encerrar el uso de un 
recurso dentro de un bloque, en donde la variable que representa al recurso vivirá unicamente dentro de ese bloque y luego de ahí su espacio
ocupado será liberado. De ese modo no nos preocupamos por cerrar el recurso manualmente una vez lo terminemos de usar. **En python esto 
sería un context manager.**

## Nest allocations

Esta sección es breve pero acá el autor marca un punto muy importante y que van más allá del tratamiento de un único recurso: **¿qué pasa
cuando un proceso consume diversos recursos?**. Se mencionan dos ideas muy importantes a mi parecer: 

* Siempre libera los recursos en un orden inverso al cual los introduciste al programa, asi no dejamos recursos huérfanos
* Siempre trae los recursos al programa en el mismo orden, asi evitamos un deadlock

Considero que es bastante importante esta mini-sección dentro del capítulo ya que siempre cuando se toca el tema nos enfocamos en un único
recurso, asi que establecer patrones cuando manejamos varios, incluso estando estos anidados, es algo bastante importante.

## Balancing exceptions

En esta subsección se menciona que los lenguajes que admiten excepciones pueden dificultar el manejo de recursos: cómo
sabemos que un recurso que introducimos al programa fue liberado al momento de ocurrir la excepción?, quedó flotando ahí?.

Comunmente nos encontramos con dos posibles formas de lidiar con las excepciones y los recursos:

* En lenguajes como Rust o C podemos encerrar a la variable que representa al recurso dentro de un bloque y una vez que la ejecución salga del bloque entonces sus recursos serán liberados
* En lenguajes como Python tenemos los famosos bloques try-except/catch-finally, en donde solemos usar el finally para asegurar el cierre del recurso

Sin embargo sobre el último punto puede surgir un problema: si introducimos al recurso dentro del bloque **try** entonces también puede surgir una excepción ahí, luego en el **finally** se intentaría liberar a un recurso que nunca fue tomado en primer lugar. La solución a esto es simplemente introducir al recurso a nuestro programa fuera del bloque try. 

Suena simple esto último, pero yo solía cometer mucho ese error incluso recientemente. Siento que es algo que ahora puedo corregir.

## When you can´t balance resources

Acá entramos en un terreno más díficil de caminar. Existen situaciones en las cuales el patrón explicado antes
de manejo de recursos puede que no funcione, más que todo en programas que son dinámicos y acceden al recurso 
en diferentes partes. 

Acá la clave que menciona el autor es **establecer una invariante semántica** que dictamine quien se encarga
de manejar los datos en el programa. Por ejemplo podríamos pensar en el caso en el cual necesitamos liberar 
una estructura de alto nivel que contiene a recursos internamente, el autor propone tres opciones:

* La estructura de alto nivel también libera a quienes viven dentro de ella
* La estructura de alto nivel simplemente se libera, dejando hijos huérfanos
* La estructura de alto nivel se niega a liberarse si contiene a alguien dentro

Esto me recuerda a como funcionan los directorios en **linux**: vos no podés borrar una carpeta 
si tiene contenido, pero si ejecutas rm -rf sobre un directorio esto va a eliminar al directorio y todo lo que 
contenga, **esto es irreversible!.**

Una de las tres opciones te puede gustar más o menos, eso depende las especificaciones de tu programa, el punto que
se quiere hacer acá es que te quedés con una de las tres y mantengas la consistencia a lo largo del programa
al momento de manejar recursos.

## Checking the balance

Acá de vuelta tenemos una subsección e intenta introducir nuestro enfoque pragmático: un programador 
pragmático no confia en nadie, incluso en si mismo, por ende se propone a escribir un componente dentro del programa
u otro programa en sí que se encargue de monitorear el manejo de recursos. 

Acá podríamos usar herramientas externas, escribir algo nosotros si lo consideramos viable o más ligero, pero el punto
de vuelta y agregar validaciones robustas que nosotros controlemos sobre como se manejan los recursos en nuestro
sistema.
