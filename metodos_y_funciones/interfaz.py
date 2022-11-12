# Pedir un numero al usuario
# - Tipo entero
# - Tipo Real


class Interfaz:
    def solicitar_numero_real(self, titulo):
        variable = input(titulo)
        try:
            variable_numerica = float(variable)
        except ValueError as error:
            print("El dato ingresado no es un numero")
            variable_numerica = 0
        return variable_numerica

    def solicitar_un_numero_entero(self, titulo):
        variable = input(titulo)
        try:
            variable_numerica = int(variable)
        except ValueError as error:
            print("El dato ingresado no es un numero")
            variable_numerica = 0
        return variable_numerica


if __name__ == "__main__":
    interfaz = Interfaz()
    numero = interfaz.solicitar_un_numero_entero("Digite su edad : ")
    print(f"la edad es {numero}")
