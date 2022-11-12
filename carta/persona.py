# Tiene
# -* nombre(texto)
# -* edad(numero entero)

# + bautizar()
# + saludar()
# + cumpleaños()


class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0

    # si no bautizamos son errores
    def bautizar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f" Hola me llamo {self.nombre} y tengo {self.edad} anos")

    def cumplir_anos(self):
        self.edad += 1


persona1 = Persona()
persona1.bautizar("Maria", 25)
persona1.saludar()
persona1.cumplir_anos()
persona1.saludar()

persona2 = Persona()
persona2.bautizar("Juan", 15)
persona2.saludar()

persona3 = Persona()
persona3.saludar()
