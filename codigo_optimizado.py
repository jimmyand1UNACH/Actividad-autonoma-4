import time
import math
import numpy as np


def es_primo(numero):
    """
    Verifica si un número es primo de forma optimizada.
    Solo revisa divisores hasta la raíz cuadrada del número.
    """
    if numero < 2:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    limite = int(math.sqrt(numero)) + 1

    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False

    return True


def buscar_primos(limite):
    """
    Busca números primos usando NumPy y list comprehension.
    """
    numeros = np.arange(1, limite + 1)

    primos = [numero for numero in numeros if es_primo(int(numero))]

    return np.array(primos)


inicio = time.time()

limite = 100000
primos_encontrados = buscar_primos(limite)

fin = time.time()

print("Búsqueda optimizada de números primos del 1 al", limite)
print("Cantidad de números primos encontrados:", len(primos_encontrados))
print("Primeros 10 números primos:", primos_encontrados[:10])
print("Últimos 10 números primos:", primos_encontrados[-10:])
print("Tiempo de ejecución:", round(fin - inicio, 4), "segundos")