"""eso"""


def sumar(valor1, valor2, valor3=0):
    suma = valor1 + valor2 + valor3
    return suma


print(sumar(2, 3, 5))
print(sumar(206, 1))
""" se puede hacer para parametros para que funcionen por defecto, darle un default"""
print(sumar(valor2=2, valor1=2))
