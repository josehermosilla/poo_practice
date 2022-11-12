def calcular_digitos(numero):
    numero = str(numero)
    lista = []
    for i in numero:
        lista.append(i)
    if "-" in lista:
        lista.remove("-")
    return len(lista)
