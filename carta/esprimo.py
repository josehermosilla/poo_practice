def es_primo(numero):
    primo = True
    contador = 2
    while contador <= numero**1 / 2 and primo:
        if numero % contador == 0:
            primo = False
        contador += 1

    return False if (numero < 2) else primo


if __name__ == "__main__":
    for i in range(1, 1001):
        if es_primo(i):
            print(i)
