"""Proyecto de lógica: katas de Python.

Cada ejercicio tiene su función o ejemplo. Al ejecutar este archivo se muestran
pruebas sencillas; los ejercicios que piden datos por teclado son opcionales.
"""

from functools import reduce
from math import pi


# EJERCICIO 1. Contar la frecuencia de cada letra de un texto sin contar espacios.
def ejercicio_1(texto):
    frecuencias = {}
    for letra in texto.lower():
        if letra != " ":
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias


# EJERCICIO 2. Obtener una lista con el doble de cada número usando map().
def ejercicio_2(numeros):
    return list(map(lambda numero: numero * 2, numeros))


# EJERCICIO 3. Encontrar palabras de una lista que contengan otra palabra.
def ejercicio_3(palabras, objetivo):
    resultado = []
    for palabra in palabras:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado


# EJERCICIO 4. Calcular diferencias entre dos listas usando map().
def ejercicio_4(lista_1, lista_2):
    if len(lista_1) != len(lista_2):
        raise ValueError("Las listas deben tener la misma longitud")
    return list(map(lambda a, b: a - b, lista_1, lista_2))


# EJERCICIO 5. Calcular la media y decir si está aprobado (nota mínima: 5).
def ejercicio_5(notas, nota_aprobado=5):
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# EJERCICIO 6. Calcular el factorial de un número de forma recursiva.
def ejercicio_6(numero):
    if numero < 0:
        raise ValueError("El factorial no admite negativos")
    if numero == 0 or numero == 1:
        return 1
    # La función se llama a sí misma hasta llegar a 1.
    return numero * ejercicio_6(numero - 1)


# EJERCICIO 7. Convertir una lista de tuplas en una lista de strings usando map().
def ejercicio_7(tuplas):
    return list(map(str, tuplas))


# EJERCICIO 8. Pedir dos números, dividirlos y manejar errores.
def ejercicio_8():
    try:
        primero = float(input("Primer número: "))
        segundo = float(input("Segundo número: "))
        print("División correcta. Resultado:", primero / segundo)
    except ValueError:
        print("Error: introduce números válidos")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")


# EJERCICIO 9. Excluir ciertas mascotas de una lista usando filter().
def ejercicio_9(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


# EJERCICIO 10. Calcular un promedio y manejar una excepción personalizada si no hay datos.
class ListaVaciaError(Exception):
    """Error para cuando intentamos calcular una media sin números."""


def ejercicio_10(numeros):
    if not numeros:
        raise ListaVaciaError("No se puede calcular la media de una lista vacía")
    return sum(numeros) / len(numeros)


# EJERCICIO 11. Pedir una edad y controlar valores no numéricos o fuera de 0 a 120.
def ejercicio_11():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120")
        print("Tu edad es:", edad)
    except ValueError as error:
        print("Edad no válida:", error)


# EJERCICIO 12. Obtener la longitud de cada palabra de una frase con map().
def ejercicio_12(frase):
    return list(map(len, frase.split()))


# EJERCICIO 13. Obtener parejas (mayúscula, minúscula) sin letras repetidas con map().
def ejercicio_13(caracteres):
    letras = []
    for caracter in caracteres:
        if caracter.isalpha() and caracter.lower() not in letras:
            letras.append(caracter.lower())
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras))


# EJERCICIO 14. Filtrar palabras que empiecen por una letra usando filter().
def ejercicio_14(palabras, letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), palabras))


# EJERCICIO 15. Crear una lambda que sume 3 a cada número de una lista.
def ejercicio_15(numeros):
    sumar_tres = lambda numero: numero + 3
    return list(map(sumar_tres, numeros))


# EJERCICIO 16. Filtrar palabras de un texto que tengan más de n letras.
def ejercicio_16(texto, n):
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


# EJERCICIO 17. Convertir una lista de dígitos en un número usando reduce().
def ejercicio_17(digitos):
    if any(not isinstance(d, int) or d < 0 or d > 9 for d in digitos):
        raise ValueError("Cada elemento debe ser un dígito entre 0 y 9")
    # Acumulamos las cifras: 5 -> 57 -> 572.
    return reduce(lambda numero, digito: numero * 10 + digito, digitos, 0)


# EJERCICIO 18. Crear estudiantes y filtrar los que tengan nota mayor o igual a 90.
def ejercicio_18():
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificación": 95},
        {"nombre": "Luis", "edad": 22, "calificación": 75},
        {"nombre": "Marta", "edad": 19, "calificación": 90},
    ]
    return list(filter(lambda alumno: alumno["calificación"] >= 90, estudiantes))


# EJERCICIO 19. Filtrar números impares de una lista con lambda.
def ejercicio_19(numeros):
    es_impar = lambda numero: numero % 2 != 0
    return list(filter(es_impar, numeros))


# EJERCICIO 20. Extraer únicamente los enteros de una lista mixta con filter().
def ejercicio_20(elementos):
    return list(filter(lambda valor: type(valor) is int, elementos))


# EJERCICIO 21. Calcular el cubo de un número utilizando lambda.
def ejercicio_21(numero):
    cubo = lambda valor: valor ** 3
    return cubo(numero)


# EJERCICIO 22. Calcular el producto de una lista numérica usando reduce().
def ejercicio_22(numeros):
    return reduce(lambda acumulado, numero: acumulado * numero, numeros, 1)


# EJERCICIO 23. Concatenar una lista de palabras utilizando reduce().
def ejercicio_23(palabras):
    return reduce(lambda texto, palabra: texto + palabra, palabras, "")


# EJERCICIO 24. Restar de forma sucesiva los valores de una lista con reduce().
def ejercicio_24(numeros):
    if not numeros:
        raise ValueError("Necesitamos al menos un número")
    return reduce(lambda total, numero: total - numero, numeros[1:], numeros[0])


# EJERCICIO 25. Contar los caracteres de una cadena de texto.
def ejercicio_25(texto):
    return len(texto)


# EJERCICIO 26. Calcular el resto de una división mediante lambda.
def ejercicio_26(a, b):
    resto = lambda primero, segundo: primero % segundo
    return resto(a, b)


# EJERCICIO 27. Calcular el promedio de una lista de números.
def ejercicio_27(numeros):
    if not numeros:
        raise ValueError("La lista está vacía")
    return sum(numeros) / len(numeros)


# EJERCICIO 28. Devolver el primer elemento repetido de una lista.
def ejercicio_28(elementos):
    vistos = []
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.append(elemento)
    return None


# EJERCICIO 29. Ocultar con # todos los caracteres salvo los cuatro últimos.
def ejercicio_29(valor):
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]


# EJERCICIO 30. Comprobar si dos palabras son anagramas.
def ejercicio_30(palabra_1, palabra_2):
    return sorted(palabra_1.lower()) == sorted(palabra_2.lower())


# EJERCICIO 31. Pedir nombres, buscar uno y lanzar excepción si no aparece.
def ejercicio_31():
    nombres = input("Escribe nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    buscado = input("¿Qué nombre quieres buscar?: ").strip()
    if buscado not in nombres:
        raise ValueError("El nombre no aparece en la lista")
    print("Nombre encontrado:", buscado)


# EJERCICIO 32. Buscar a un empleado por nombre completo y devolver su puesto.
def ejercicio_32(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return "Esta persona no trabaja aquí"


# EJERCICIO 33. Sumar elementos de dos listas en la misma posición usando lambda.
def ejercicio_33(lista_1, lista_2):
    if len(lista_1) != len(lista_2):
        raise ValueError("Las listas deben tener la misma longitud")
    sumar = lambda a, b: a + b
    return list(map(sumar, lista_1, lista_2))


# EJERCICIO 34. Crear la clase Arbol y sus métodos para tronco y ramas.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for posicion in range(len(self.ramas)):
            self.ramas[posicion] += 1

    def quitar_rama(self, posicion):
        # Posiciones numeradas desde 1 para seguir el caso de uso del enunciado.
        if posicion < 1 or posicion > len(self.ramas):
            raise IndexError("Esa rama no existe")
        self.ramas.pop(posicion - 1)

    def info_arbol(self):
        return {"tronco": self.tronco, "numero_ramas": len(self.ramas),
                "longitudes_ramas": self.ramas.copy()}


# EJERCICIO 35. No aparece en el PDF del enunciado; no se inventa uno.


# EJERCICIO 36. Crear la clase UsuarioBanco con ingresos, retiradas y transferencias.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError("El usuario no tiene cuenta corriente")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.saldo:
            raise ValueError("No hay saldo suficiente")
        self.saldo -= cantidad

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.saldo += cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        # El dinero sale de otro_usuario y entra en el usuario actual.
        if not self.cuenta_corriente:
            raise ValueError("El destinatario no tiene cuenta corriente")
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)


# EJERCICIO 37. Procesar texto: contar, reemplazar o eliminar palabras.
def contar_palabras(texto):
    contador = {}
    for palabra in texto.split():
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    palabras = texto.split()
    return " ".join(palabra_nueva if p == palabra_original else p for p in palabras)


def eliminar_palabra(texto, palabra):
    return " ".join(p for p in texto.split() if p != palabra)


def procesar_texto(texto, opcion, *argumentos):
    if opcion == "contar" and len(argumentos) == 0:
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(argumentos) == 2:
        return reemplazar_palabras(texto, argumentos[0], argumentos[1])
    elif opcion == "eliminar" and len(argumentos) == 1:
        return eliminar_palabra(texto, argumentos[0])
    else:
        raise ValueError("Opción o número de argumentos no válido")


# EJERCICIO 38. Indicar si es de día, tarde o noche según una hora dada.
def ejercicio_38():
    try:
        hora = int(input("Introduce la hora (0-23): "))
        if hora < 0 or hora > 23:
            print("Hora no válida")
        elif 6 <= hora < 12:
            print("Es de día")
        elif 12 <= hora < 20:
            print("Es de tarde")
        else:
            print("Es de noche")
    except ValueError:
        print("Debes introducir una hora entera")


# EJERCICIO 39. Pasar de una calificación numérica a una descripción.
def ejercicio_39(nota):
    if not 0 <= nota <= 100:
        return "Nota no válida"
    if nota < 70:
        return "insuficiente"
    elif nota < 80:
        return "bien"
    elif nota < 90:
        return "muy bien"
    else:
        return "excelente"


# EJERCICIO 40. Calcular el área de rectángulo, círculo o triángulo.
def ejercicio_40(figura, datos):
    if figura == "rectangulo" and len(datos) == 2:
        area = datos[0] * datos[1]
    elif figura == "circulo" and len(datos) == 1:
        area = pi * datos[0] ** 2
    elif figura == "triangulo" and len(datos) == 2:
        area = datos[0] * datos[1] / 2
    else:
        raise ValueError("Figura o datos incorrectos")
    if any(dato < 0 for dato in datos):
        raise ValueError("Las medidas no pueden ser negativas")
    return area


# EJERCICIO 41. Pedir precio y cupón y calcular el total de la compra.
def ejercicio_41():
    try:
        precio = float(input("Precio original (€): "))
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        respuesta = input("¿Tienes un cupón? (sí/no): ").strip().lower()
        if respuesta in ("sí", "si"):
            descuento = float(input("Valor del cupón (€): "))
            if descuento > 0:
                precio_final = max(0, precio - descuento)
            else:
                print("El cupón no es válido: no se aplica descuento")
                precio_final = precio
        elif respuesta == "no":
            precio_final = precio
        else:
            print("Respuesta no reconocida: no se aplica descuento")
            precio_final = precio
        print(f"Precio final: {precio_final:.2f} €")
    except ValueError as error:
        print("Dato incorrecto:", error)


# PRUEBAS. Estos ejemplos permiten comprobar las katas sin escribir datos.
def mostrar_ejemplos():
    print("1:", ejercicio_1("Hola hola"))
    print("2:", ejercicio_2([1, 2, 3]))
    print("3:", ejercicio_3(["casita", "casa", "perro"], "casa"))
    print("4:", ejercicio_4([8, 7], [3, 2]))
    print("5:", ejercicio_5([6, 8, 4]))
    print("6:", ejercicio_6(5))
    print("7:", ejercicio_7([(1, 2), (3, 4)]))
    print("9:", ejercicio_9(["Gato", "Tigre", "Perro"]))
    try:
        print("10:", ejercicio_10([]))
    except ListaVaciaError as error:
        print("10: Error controlado:", error)
    print("12:", ejercicio_12("Me gusta Python"))
    print("13:", ejercicio_13("aBbAc"))
    print("14:", ejercicio_14(["sol", "silla", "luna"], "s"))
    print("15:", ejercicio_15([1, 2, 3]))
    print("16:", ejercicio_16("Hoy aprendemos Python", 4))
    print("17:", ejercicio_17([5, 7, 2]))
    print("18:", ejercicio_18())
    print("19:", ejercicio_19([1, 2, 3, 4]))
    print("20:", ejercicio_20([1, "dos", 3, "cuatro"]))
    print("21:", ejercicio_21(3))
    print("22:", ejercicio_22([2, 3, 4]))
    print("23:", ejercicio_23(["Hola", " ", "mundo"]))
    print("24:", ejercicio_24([10, 3, 2]))
    print("25:", ejercicio_25("Python"))
    print("26:", ejercicio_26(10, 3))
    print("27:", ejercicio_27([5, 7, 9]))
    print("28:", ejercicio_28([1, 2, 3, 2]))
    print("29:", ejercicio_29("123456789"))
    print("30:", ejercicio_30("roma", "amor"))
    empleados = [{"nombre": "Ana García", "puesto": "Diseñadora"},
                 {"nombre": "Luis Pérez", "puesto": "Analista"}]
    print("32:", ejercicio_32("Ana García", empleados))
    print("33:", ejercicio_33([1, 2], [3, 4]))

    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    print("34:", arbol.info_arbol())

    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)
    try:
        alicia.transferir_dinero(bob, 80)
    except ValueError as error:
        print("36: Transferencia no realizada:", error)
    # El ejemplo pide transferir 80 desde Bob, pero Bob solo tiene 70.
    # Por eso se muestra el error y los saldos no cambian.
    alicia.retirar_dinero(50)
    print("36: Saldos:", alicia.saldo, bob.saldo)

    texto = "hola mundo hola"
    print("37 contar:", procesar_texto(texto, "contar"))
    print("37 reemplazar:", procesar_texto(texto, "reemplazar", "hola", "adiós"))
    print("37 eliminar:", procesar_texto(texto, "eliminar", "hola"))
    print("39:", ejercicio_39(85))
    print("40:", ejercicio_40("circulo", (2,)))


if __name__ == "__main__":
    mostrar_ejemplos()
    respuesta = input("¿Quieres probar los ejercicios interactivos? (sí/no): ").strip().lower()
    if respuesta in ("si", "sí"):
        # Solo estas katas requieren escribir datos en la consola.
        for numero, funcion in [(8, ejercicio_8), (11, ejercicio_11),
                                (31, ejercicio_31), (38, ejercicio_38), (41, ejercicio_41)]:
            print(f"\nEjercicio {numero}")
            try:
                funcion()
            except ValueError as error:
                print("Error controlado:", error)
