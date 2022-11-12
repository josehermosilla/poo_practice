"""
Clase Persona
Con un nombre y una edad
Una funcionalidad que permita a la persona cumplir años
Una funcionalidad que permita a la persona saludar

"""


class Persona:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad}")

    def cumpliranyos(self):
        self.edad += 1


persona1 = Persona("Maria", 22)
persona1.saludar()
persona1.cumpliranyos()
persona1.saludar()
