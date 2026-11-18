# Proyecto de lógica: Katas de Python 🐍

## ¿En qué consiste el proyecto?

Este repositorio recoge mis soluciones a las katas de Python del proyecto de lógica. He intentado resolverlas de manera sencilla para practicar lo que he aprendido durante el curso y entender cómo funciona cada paso.

## ¿Qué he practicado?

- Variables y tipos de datos (`int`, `float`, `str`, listas, tuplas y diccionarios).
- Condicionales `if`, `elif` y `else`.
- Bucles `for`.
- Funciones, parámetros y valores de retorno.
- Funciones `map()`, `filter()`, `reduce()` y expresiones `lambda`.
- Excepciones con `try` y `except`.
- Clases, objetos, atributos y métodos.
- Importación de módulos (`functools` y `math`).

## Archivos

- `katas.py`: soluciones con el enunciado resumido en un comentario antes de cada ejercicio y ejemplos para probarlas.
- `README.md`: explicación del proyecto y de cómo ejecutarlo.

## Pasos que he seguido

1. Leer cada ejercicio y pensar qué datos entran y qué resultado debe salir.
2. Crear una función por ejercicio cuando tenía sentido, para poder probarla con valores diferentes.
3. Usar `map()`, `filter()`, `reduce()` o `lambda` cuando lo pide el enunciado.
4. Añadir condiciones y control de errores en los ejercicios que lo necesitan.
5. Crear las clases `Arbol` y `UsuarioBanco` y probar sus métodos siguiendo los ejemplos propuestos.
6. Añadir ejemplos al final del archivo y ejecutar el programa para comprobar las soluciones.

## Cómo ejecutarlo

Necesitas tener Python 3 instalado. No es necesario instalar librerías externas.

1. Descarga este repositorio desde GitHub o clónalo en tu equipo.
2. Abre una terminal dentro de la carpeta del proyecto.
3. Ejecuta:

```bash
python katas.py
```

En algunos equipos hay que usar `python3 katas.py`.

Primero aparecen ejemplos de los ejercicios. Después, el programa pregunta si quieres probar los ejercicios interactivos (8, 11, 31, 38 y 41), que necesitan escribir respuestas por teclado.

## Cosas que me han hecho pensar

- **Recursividad (6):** entendí que el factorial se puede calcular llamando a la misma función, pero hay que indicar cuándo parar.
- **`reduce()` (17, 22, 23 y 24):** sirve para ir combinando los elementos de una lista hasta conseguir un solo resultado.
- **Excepciones (8, 10, 11 y 36):** ayudan a mostrar un error claro cuando no se puede hacer una operación.
- **Clases (34 y 36):** agrupan información y acciones relacionadas en un mismo objeto.

## Detalles importantes del enunciado

- **El ejercicio 35 no aparece en el PDF:** después del 34 pasa directamente al 36. He dejado indicado este salto en `katas.py`, sin inventar un ejercicio.
- **Ejercicio 36:** Bob empieza con 50 y recibe 20, así que tiene 70. Por tanto, la transferencia de 80 a Alicia no se puede hacer. He respetado la indicación de lanzar un error si una operación no es posible. Alicia sí puede retirar sus 50 después.
- **Ejercicio 34:** interpreto la posición 2 de una rama como la segunda rama (contando desde 1).
- **Ejercicio 38:** el enunciado no fija los horarios; he utilizado día de 6:00 a 11:59, tarde de 12:00 a 19:59 y noche de 20:00 a 5:59.
- **Ejercicio 40:** el área del rectángulo usa (base, altura), la del círculo (radio,) y la del triángulo (base, altura).

## Antes de entregar

Comprueba que puedes ejecutar `katas.py`, revisa que entiendes los ejemplos y sube esta carpeta a un **repositorio público de GitHub**. Después, pega el enlace del repositorio en el espacio de entrega del curso.
