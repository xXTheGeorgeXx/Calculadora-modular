import math
from collections import Counter

# --- Aritmética ---
def sumar(lista):
    return sum(lista)

def restar(a, b):
    return a - b

def multiplicar(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(n)

def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a % b

def maximo(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    return max(lista)

def minimo(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    return min(lista)

def redondear(numero, decimales=2):
    return round(numero, decimales)

def operar_expresion(expresion):
    try:
        return eval(expresion)
    except Exception:
        raise ValueError("Expresión matemática inválida.")
# --- Científicas ---
def logaritmo(n):
    if n <= 0:
        raise ValueError("El logaritmo solo está definido para números positivos.")
    return math.log10(n)

# --- Trigonometría inversa (en grados) ---
def arco_seno(x):
    if -1 <= x <= 1:
        return math.degrees(math.asin(x))
    else:
        raise ValueError("El valor debe estar entre -1 y 1 para arco seno.")

def arco_coseno(x):
    if -1 <= x <= 1:
        return math.degrees(math.acos(x))
    else:
        raise ValueError("El valor debe estar entre -1 y 1 para arco coseno.")

def arco_tangente(x):
    return math.degrees(math.atan(x))

# --- Funciones hiperbólicas ---
def seno_hiperbolico(x):
    return math.sinh(x)

def coseno_hiperbolico(x):
    return math.cosh(x)

def tangente_hiperbolica(x):
    return math.tanh(x)

# --- Combinatoria ---
def factorial(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError("El factorial solo está definido para enteros no negativos.")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def combinacion(n, k):
    if not (isinstance(n, int) and isinstance(k, int)):
        raise ValueError("n y k deben ser enteros.")
    if k > n or n < 0 or k < 0:
        raise ValueError("Valores inválidos para n y k.")
    return factorial(n) // (factorial(k) * factorial(n - k))

def permutacion(n, k):
    if not (isinstance(n, int) and isinstance(k, int)):
        raise ValueError("n y k deben ser enteros.")
    if k > n or n < 0 or k < 0:
        raise ValueError("Valores inválidos para n y k.")
    return factorial(n) // factorial(n - k)

# --- Estadística ---
def promedio_lista(lista):
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")
    return sum(lista) / len(lista)

def mediana(lista):
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    medio = n // 2
    if n % 2 == 0:
        return (lista_ordenada[medio - 1] + lista_ordenada[medio]) / 2
    else:
        return lista_ordenada[medio]

def moda(lista):
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")
    contador = Counter(lista)
    max_count = max(contador.values())
    modas = [k for k, v in contador.items() if v == max_count]
    if len(modas) == len(contador):
        return None  # No hay moda si todos los valores aparecen igual número de veces
    return modas if len(modas) > 1 else modas[0]

def varianza(lista):
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")
    media = promedio_lista(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista)

def desviacion_estandar(lista):
    return math.sqrt(varianza(lista))