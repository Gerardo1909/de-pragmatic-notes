# Dead programs tell no lies - the pragmatic programmer (20 aniversario)

> "Los programas muertos no dicen mentiras" seria su traducción al español. 

Este subtema (o capítulo) perteneciente al libro "The Pragmatic Programmer" habla sobre el manejo de 
excepciones durante la ejecución de un programa, menciona que hay muchas ocasiones en las que ni nosotros
mismos nos damos cuenta sobre lo que está mal con nuestro código y tendemos a pensar que el caso 
impensado "nunca va a pasar" (i.e algún dato corrupto, una conexión que se nos olvidó cerrar, etc.). 

###  Catch and release is for fish 

Luego habla sobre como trabajar a las excepciones y menciona el caso clásico (en el cual yo también he 
llegado a caer) el cual consiste en tomar una excepción que lanza un método al cual llamamos y re-lanzarlo 
haciendole algún procesamiento o simplemente mostrando el mensaje de error por consola. El problema
con este enfoque es que nuestro código **se hace mucho más verboso** (en si un bloque try-catch/except es verboso) y el mantenimiento se hace mucho más difícil. 

* Podemos pensar que por cada nueva excepción que lance el programa que invocamos nosotros 
deberiamos capturarla en el bloque catch/except, escribir código adicional para ese caso 
aplicando la misma lógica que habiamos aplicado con otros errores y rompiendo uno de los principios
más famosos en el mundo del software: **Open-Closed.**

El enfoque correcto según el libro entonces sería **simplemente llamar al método que vamos a utilizar 
y dejarlo que explote**. Esto logra que nuestro código sea mucho más simple y menos verboso, además 
de desacoplar la lógica del método que llama con respecto a la del método llamado (en el enfoque 
clásico la función que llama sabe sobre los errores que lanza la función llamada).

###  Crash, don´t trash

Otro de los temas que trata el capítulo en torno a las excepciones es la idea de crashear lo más pronto 
posible, con lo cual yo personalmente concuerdo. La otra alternativa a este enfoque es evidentemente 
seguir con la ejecución del programa y escribir a los datos corruptos en una base de datos que necesite
su información de todos modos. 

A primera impresión, cuando leí este fragmento en el capítulo me generó impresión de que no seguía la 
temática que veníamos tratando con lo de la programación a la defensiva, pero creo que la conexión está
en la idea de que si usamos el enfoque común que describe la sección anterior (atrapar a todas las 
excepciones que lance un método invocado y re-lanzarlas) podríamos llegar a silenciar errores que 
a lo mejor nos interesan, o peor aún, ignorarlos lleva silenciosamente al programa a un estado corrupto. 
De ahí que la siguiente sección hablara sobre **fallar rápido**.

Sin embargo, en el capítulo se menciona que en algunos casos el terminar un programa puede ser inapropiado ya que podríamos no liberar un recurso que debería ser utilizado por otro componente del sistema y eso haria que el error potencialmente provoque una reacción en cadena, o simplemente debamos escribir un log incluso
ante error (es lo que yo más he visto).

Sin embargo sigue siendo el mismo: si en el código ocurre algo que creíamos imposible entonces es porque 
el programa entró en un estado "inviable" y por ende deberíamos finalizarlo ya que todo lo que ocurra luego
de esa situación es sospechoso.

> Un programa "muerto" normalmente hace menos daño que uno corrupto.
