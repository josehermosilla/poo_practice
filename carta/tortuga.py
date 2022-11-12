"""metodos permitidos en turtle
forward -> fd
backward -> bk
right -> rt
left ->lt 
"""
import turtle


def dibujar_poligonos(lados=4, tamano=100):
    dibujo = turtle.Turtle()
    dibujo.color("black", "green")
    dibujo.begin_fill()
    angulo = 360.0 / lados
    for i in range(0, lados + 1):
        dibujo.forward(tamano)
        dibujo.right(angulo)
    dibujo.end_fill()  # al finalizar el dibujo se pinta
    turtle.done()


if __name__ == "__main__":
    dibujar_poligonos(20, 40)
