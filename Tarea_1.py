# Elaborado por:Carlos Herrera Martinez,
# Fecha de creacion:3/8/2021 10:20
# ERR3 -1.5 Repitio el mismo error

# Importacion de libreias
from math import factorial
# Definicion de funciones


def Validar1(string):
    """
    Funcionalidad:
    Entradas:
    Salidas:
    """
    if string.isdigit():
        return True
    else:
        return False


def multiple_op(x):
    """
    Funcionalidad:
    Esta funcion recibe como parametro x y retorna las
    siguiente operaciones x*x, 2^x y x! en un array
    Entradas:x(strg):parametro de entrada
    Salidas
    resultado(lista): retorna una arreglo con los resultados de las
    siguientes operaciones x*x, 2^x y x!
    """
    if(Validar1(str(x))):
        i = x*x
        ii = 2**x
        iii = factorial(x)
        resultado = [i, ii, iii]
        return resultado
    else:
        return ValueError


def verify_array_op(lista):
    """
    Funcionalidad:
    Entradas:
    Salidas
    """
    i = 0
    salida = []
    while(i < len(lista)):
        dato = multiple_op(lista[i])
        if (dato == ValueError):
            return ValueError
        else:
            salida.append(dato)
        i = i+1
    return salida
