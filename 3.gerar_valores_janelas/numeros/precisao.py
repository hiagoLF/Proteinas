from pandas import DataFrame

def diminuirPrecisaoDeNumeros(numeros: list):
    numeros = []
    for numero in numeros:
        numeros.append(round(numero, 3))
    return numeros