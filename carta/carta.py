# abrimos un bloque de codigo
class Carta:
    # metodo constructor, se ejecuta una vez que instanciamos la clase
    def __init__(self, numero, palo):
        self.palo = palo
        self.numero = numero

    # metodo para imprimir el contenido de la carta (el self indica que es un metodo de la clase)
    def imprimir(self):
        numero = self.convertir_numero_a_letras()
        print(numero, "de", self.palo)

    def convertir_numero_a_letras(self):
        valor = ""
        if (self.numero) == 11:
            valor = "J"
        elif self.numero == 12:
            valor = "Q"
        elif self.numero == 13:
            valor = "K"
        elif self.numero == 1:
            valor = "As"
        else:
            valor = str(self.numero)
        return valor


def main():
    carta = Carta(11, "Treboles")
    carta.imprimir()
    carta = Carta(12, "Treboles")
    carta.imprimir()
    carta = Carta(13, "Treboles")
    carta.imprimir()
    carta = Carta(1, "Treboles")
    carta.imprimir()

    carta = Carta(4, "Treboles")
    carta.imprimir()

    carta = Carta(8, "Treboles")
    carta.imprimir()


if __name__ == "__main__":
    main()
