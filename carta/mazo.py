from carta import Carta


class Mazo:
    def __init__(self):
        self.crear_mazo()

    def crear_mazo(self):
        for j in range(1, 5):
            for i in range(1, 14):
                carta = Carta(i, self.retornar_palo(j))
                carta.imprimir()

    def retornar_palo(self, i):
        palo = ""
        if i == 1:
            palo = "Treboles"
        elif i == 2:
            palo = "Diamantes"
        elif i == 3:
            palo = "Corazones"
        elif i == 4:
            palo = "Espadas"
        return palo


mazo1 = Mazo()
