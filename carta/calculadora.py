class Calculadora:
    def calcular_factorial(self, numero):
        # 4! => 1 * 2 *3 * 4
        resultado = None
        if numero >= 0:
            resultado = 1
            for i in range(1, (numero + 1)):
                resultado *= i
        return resultado

    def calcular_coseno(self, x, n):
        if n < 0:
            return 0
        resultado = 1
        contador = 2
        signo = -1
        if n % 2 != 0:
            n += 1

        while contador <= n:
            numerador = x**contador
            denominador = self.calcular_factorial(contador)
            fraccion = signo * numerador / denominador
            resultado += fraccion
            contador += 2
            signo *= -1
        return resultado

    def calcular_seno(self, x, n):
        if n < 0:
            return 0
        resultado = 0
        contador = 1
        signo = 1
        if n % 2 == 0:
            n += 1
        while contador <= n:
            numerador = x**contador
            denominador = self.calcular_factorial(contador)
            fraccion = signo * numerador / denominador
            resultado += fraccion
            contador += 2
            signo *= -1
        return resultado


calculadora = Calculadora()
print("Calculo del coseno:", calculadora.calcular_coseno(2, 8))
print("Calculo del factorial:", calculadora.calcular_factorial(5))
print("Calculo del coseno:", calculadora.calcular_coseno(2, 8))
print("Calculo del coseno:", calculadora.calcular_coseno(-1, -2))
print("Calculo del coseno:", calculadora.calcular_seno(5, 6))
