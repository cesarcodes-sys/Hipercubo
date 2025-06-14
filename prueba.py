import turtle
import threading

# Crear la ventana de dibujo
ventana = turtle.Screen()

# Crear las tortugas
tortuga1 = turtle.Turtle()
tortuga2 = turtle.Turtle()

# Definir las animaciones de las tortugas
def animacion_tortuga1():
    for _ in range(4):
        tortuga1.forward(100)
        tortuga1.right(90)

def animacion_tortuga2():
    for _ in range(3):
        tortuga2.forward(100)
        tortuga2.left(120)

# Crear los hilos para las animaciones
hilo_tortuga1 = threading.Thread(target=animacion_tortuga1)
hilo_tortuga2 = threading.Thread(target=animacion_tortuga2)

# Iniciar los hilos
hilo_tortuga1.start()
hilo_tortuga2.start()

# Cerrar la ventana al hacer clic en ella
ventana.exitonclick()
