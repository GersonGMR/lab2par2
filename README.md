# Repositorio laboratorio y parcial dos SE
Repositorio destinado para la repetición del parcial y laboratorio dos de la materia sistemas expertos de la facultad de ingeniería de la Universidad Evangélica de El Salvador.

## Rama Desarrollo1
Desarrollo del laboratio dos de la materia de sistemas expertos. Lo que nos solicitan:
1. Mostrar en pantalla que el usuario tiene 2 opciones: 
- Especificar nombre de archivo y procesar su contenido
- Salir del programa
2. Si el usuario elige la primera opción se debe capturar el nombre del archivo, informar al
usuario que se pudo leer o no la entrada de datos; en caso que la fuente de datos no pudo
leerse informar al usuario que vuelva a intentar y se regresa al menu de opciones principal.
3. El nombre del archivo debe ser enviado al programa de procesamiento de contenido como
un parámetro.
4. Leer archivos en texto sin importar la extensión de éste (json, txt, sin extensión, otros).
5. Informar al usuario de los siguientes resultados en base al archivo facilitado por el usuario:
- Número de caracteres (se incluyen espacios en blanco)
- Número de palabras (separados por espacios en blanco)
- Número de líneas
- Número de palabras únicas (“NO” es diferente de “no”)
6. Codificar la solución utilizando estructuras de control y estructuras de datos de su elección,
debe informarse al usuario sobre el tiempo de ejecución utilizado hasta mostrar los
resultados especificados en el numeral 5. Se sugiere que su solución sea desarrollada en
ambiente de consola.
7. Se requiere aplicar todos los estándares de buenas prácticas de codificación desarrollados
en las sesiones de trabajo de la unidad 2.

## Flujo de datos de rama desarrollo1
1. Se muestra al usuario un menú con dos opciones.
- Ingresar el nombre del archivo
- Salir
2. Si el usuario ingresa el nombre del archivo pasamos a analizarlo
3. Se realizan las operaciones para calcular la cantidad de palabras,caracteres,filas y palabras únicas contenidas en el archivo proporcionado.
4. Se muestran los resultados de las operaciones anteriores y el tiempo de ejecución del programa.
5. Volvemos al menú principal
6. Si el usuario escoge la opción dos, el programa se finaliza.

## Rama desarrollo2
Desarrollo del parcial dos de la materia de sistemas expertos. Lo que nos solicitan:
1. Mostrar en pantalla que el usuario tiene 2 opciones: 
- Especificar nombre de archivo y procesar su contenido
- Salir del programa
2. Si el usuario elige la primera opción se debe capturar el nombre del archivo, informar al
usuario que se pudo leer o no la entrada de datos; en caso que la fuente de datos no pudo
leerse informar al usuario que vuelva a intentar y se regresa al menu de opciones principal.
3. El nombre del archivo debe ser enviado al programa de procesamiento de contenido como
un parámetro.
4. Leer archivos en texto sin importar la extensión de éste (json, txt, sin extensión, otros).
5. Informar al usuario de los siguientes resultados en base al archivo facilitado por el usuario:
- Número de caracteres (se incluyen espacios en blanco)
- Número de palabras (separados por espacios en blanco)
- Número de líneas
- Número de palabras únicas (“NO” es diferente de “no”)
6. Codificar la solución utilizando estructuras de control y estructuras de datos de su elección,
debe informarse al usuario sobre el tiempo de ejecución utilizado hasta mostrar los
resultados especificados en el numeral 5. Se sugiere que su solución sea desarrollada en
ambiente de consola.
7. Se requiere aplicar todos los estándares de buenas prácticas de codificación desarrollados
en las sesiones de trabajo de la unidad 2.

## Flujo de datos de la rama Desarrollo2
1. Menu principal.
- Ingresar el nombre del archivo
  - Si el usuario ingresa el nombre del archivo pasamos a validar que el archivo si existe.
    - El archivo existe
      - Se realizan las operaciones para calcular la cantidad de palabras,caracteres,filas y palabras únicas contenidas en el archivo proporcionado. 
      - Se muestran los resultados de las operaciones anteriores y el tiempo de ejecución del programa y volvemos al menu principal
    - El archivo no existe
      - Se envía el mensaje al usuario " El archivo no existe " y volvemos al menu principal
  - Salir
    - Salimos del programa
 - Si el usuario ingresa un numero diferente de 1 y 2 se le solicita que ingrese un numero válido entre 1 y 2.
 - Si el usuario ingresa un valor diferente de un valor entero, se le envía el mensaje "Introduce un numero entero del menu: "

