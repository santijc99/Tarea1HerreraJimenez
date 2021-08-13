# Elaborado por:Carlos Herrera Martinez,
# Fecha de creacion:3/8/2021 10:20

# Importacion de libreias
import random
import string
from math import factorial
from Tarea_1 import multiple_op
from Tarea_1 import verify_array_op


# Definicion de funciones
def test_multiple_op():
    a = random.randint(0, 5)
    assert multiple_op(a) == [a*a, 2**a, factorial(a)]


def test_verify_array_op():
    a = random.randint(0, 5)
    b = random.randint(0, 5)
    c = random.randint(0, 5)
    test_lista = [a, b, c]
    assert verify_array_op(test_lista) == [[a*a, 2**a, factorial(a)],
                                           [b*b, 2**b, factorial(b)],
                                           [c*c, 2**c, factorial(c)]]


def test_multiple_op2():
    a = random.randint(0, 25)
    stringcompleto = string.ascii_lowercase
    assert multiple_op(stringcompleto[a]) == ValueError


def test_verify_array_op2():
    stringcompleto = string.ascii_lowercase
    test_lista = []
    i = 0
    while(i < 3):
        a = random.randint(0, 25)
        test_lista.append(stringcompleto[a])
        i += 1
    assert verify_array_op(test_lista) == ValueError
