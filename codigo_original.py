
import time


def es_primo(numero):
    """
    Verifica si un número es primo.
    Esta versión es intencionalmente lenta porque revisa todos los divisores
    desde 2 hasta numero - 1.
    """
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True


def buscar_primos(limite):
    """
    Busca todos los números primos desde 1 hasta el límite indicado.
    """
    primos = []

    for numero in range(1, limite + 1):
        if es_primo(numero):
            primos.append(numero)

    return primos


# Inicio de medición del tiempo
inicio = time.time()

limite = 100000
primos_encontrados = buscar_primos(limite)

# Fin de medición del tiempo
fin = time.time()

print("Búsqueda de números primos del 1 al", limite)
print("Cantidad de números primos encontrados:", len(primos_encontrados))
print("Primeros 10 números primos:", primos_encontrados[:10])
print("Últimos 10 números primos:", primos_encontrados[-10:])
print("Tiempo de ejecución:", round(fin - inicio, 4), "segundos")