import threading
import time
from tkinter import messagebox
from turtle import *
from tkinter import *
import turtle
import random

class Nodo:
    def __init__(self,x,y,horizontal,arco,vertical,diagonalx,diagonaly,nombre):
        self.x = x
        self.y = y
        self.h = horizontal
        self.a = arco
        self.v = vertical
        self.dx = diagonalx
        self.dy = diagonaly
        self.nombre = nombre

def xor(x, y):
    ans = ""

    for i in range(len(x)):
        if x[i] == "0" and y[i] == "1" or x[i] == "1" and y[i] == "0":

            ans += "1"
        else:
            ans += "0"
    return ans

#Opotimizar el metodo 
def ruta():
    turtle.setup(1200, 800, 0, 0)
    turtle.screensize(400, 400)
    turtle.clearscreen()
    turtle.pensize(4)
    turtle.color("black")

    x1 = entradae1.get()
    y1 = entradad1.get()
    x2 = entradae2.get()
    y2 = entradad2.get()

    try:
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if x1 < 0 or x1 > 15 or y1 < 0 or y1 > 15 or x2 < 0 or x2 > 15 or y2 < 0 or y2 > 15:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Los valores deben ser enteros en el rango del 0 al 15.")
        return

    bx1 = format(x1, '04b')  # Convierte x1 a binario con formato de 4 dígitos
    by1 = format(y1, '04b')  # Convierte y1 a binario con formato de 4 dígitos
    bx2 = format(x2, '04b')  # Convierte x2 a binario con formato de 4 dígitos
    by2 = format(y2, '04b')  # Convierte y2 a binario con formato de 4 dígitos

    #Modificar
    turtle.write("\n" + "\n\n\n" + "Ruta 1 del nodo : " + str(x1) + " al nodo : " + str(y1) + "\n"
                 + "Ruta 2 del nodo : " + str(x2) + " al nodo : " + str(y2) + "\n\n" +
                 "           3210" + "\nTAG1: " + xor(bx1, by1) + "\nTAG2: " + xor(bx2, by2) +
                 "\n\n" + " Salto: 3 \n Vertical: 2 \n Diagonal: 1 \nHorizontal: 0 \n\n\n ")

    tag1 = xor(bx1, by1)
    camino1 = determinarRuta(tag1)
    random.shuffle(camino1)

    #Modificar
    #turtle.write("\n" + "\n\n\n" + "Del nodo : " + str(x2) + " al nodo : " + str(y2) + "\n\n\n" +
    #         "          3210" + "\n TAG: " + xor(bx2, by2) + "\n\n" + " Salto: 3 \n Vertical: 2 \n Diagonal: 1 \nHorizontal: 0 \n\n\n ")
    tag2 = xor(bx2, by2)
    camino2 = determinarRuta(tag2)
    random.shuffle(camino2)

    turtle.speed(2500)
    lado = 200
    arc = 600
    diagonal = 120

    nodos = []

    nodos.append(Nodo(-300,100,lado,arc,-lado,-diagonal,-diagonal,"#0 \n 0000"))
    nodos.append(Nodo(-100,100,-lado,arc,-lado,-diagonal,-diagonal,"#1 \n 0001"))
    nodos.append(Nodo(-420,-20,lado,arc,-lado,diagonal,diagonal,"#2 \n\n 0010"))
    nodos.append(Nodo(-220,-20,-lado,arc,-lado,diagonal,diagonal,"#3 \n\n 0011"))
    nodos.append(Nodo(-300,-100,lado,arc,lado,-diagonal,-diagonal,"#4 \n 0100"))
    nodos.append(Nodo(-100,-100,-lado,arc,lado,-diagonal,-diagonal,"#5 \n 0101")) 
    nodos.append(Nodo(-420,-220,lado,arc,lado,diagonal,diagonal,"#6 \n\n 0110")) 
    nodos.append(Nodo(-220,-220,-lado,arc,lado,diagonal,diagonal,"#7 \n\n 0111")) 

    incx = 600
    nodos.append(Nodo(-300 + incx,100,lado,-arc,-lado,-diagonal,-diagonal,"#8 \n 1000")) 
    nodos.append(Nodo(-100 + incx,100,-lado,-arc,-lado,-diagonal,-diagonal,"#9 \n 1001")) 
    nodos.append(Nodo(-420 + incx,-20,lado,-arc,-lado,diagonal,diagonal,"#10 \n\n 1010")) 
    nodos.append(Nodo(-220 + incx,-20,-lado,-arc,-lado,diagonal,diagonal,"#11 \n\n 1011")) 
    nodos.append(Nodo(-300 + incx,-100,lado,-arc,lado,-diagonal,-diagonal,"#12 \n 1100")) 
    nodos.append(Nodo(-100 + incx,-100,-lado,-arc,lado,-diagonal,-diagonal,"#13 \n 1101")) 
    nodos.append(Nodo(-420 + incx,-220,lado,-arc,lado,diagonal,diagonal,"#14 \n\n 1110")) 
    nodos.append(Nodo(-220 + incx,-220,-lado,-arc,lado,diagonal,diagonal,"#15 \n\n 1111")) 

    for n in nodos:
        regresa(n)
        dot(10, "blue")
        goto(n.x + 20, n.y + 5)
        write(n.nombre)
        regresa(n)
        goto(n.x + n.h, n.y)
        regresa(n)
        goto(n.x, n.y + n.v)
        regresa(n)
        goto(n.x + n.dx, n.y + n.dy)
        regresa(n)

    turtle1 = turtle.Turtle()
    turtle1.shape("turtle")
    turtle1.color("blue")
    turtle1.pensize(8)

    turtle2 = turtle.Turtle()
    turtle2.shape("turtle")
    turtle2.color("green")
    turtle2.pensize(8)

    nodoActual1 = nodos[int(bx1, 2)]
    nodoActual2 = nodos[int(bx2, 2)]

    turtle1.penup()
    turtle1.goto(nodoActual1.x, nodoActual1.y)
    turtle1.pendown()

    turtle2.penup()
    turtle2.goto(nodoActual2.x, nodoActual2.y)
    turtle2.pendown()

    turtle1.dot(20, "blue")
    turtle2.dot(20, "green")

    hilo_tortuga1 = threading.Thread(target=animaciont1, args=(camino1, turtle1, nodos, nodoActual1))
    hilo_tortuga2 = threading.Thread(target=animaciont2, args=(camino2, turtle2, nodos, nodoActual2))


    hilo_tortuga1.start()
    hilo_tortuga2.start()


    turtle.done()
       
def animaciont1(camino1, turtle1, nodos, nodoActual1):
    for item1 in camino1:
        turtle1.speed(2)

        if item1 == "Salto":
            turtle1.goto(nodoActual1.x, nodoActual1.y + 100)
            nodoActual1 = actualizaNodo(nodoActual1.x + nodoActual1.a, nodoActual1.y, nodos)
            turtle1.goto(nodoActual1.x, nodoActual1.y + 100)
            turtle1.goto(nodoActual1.x, nodoActual1.y)
        if item1 == "Vertical":
            nodoActual1 = actualizaNodo(nodoActual1.x, nodoActual1.y + nodoActual1.v, nodos)
            turtle1.goto(nodoActual1.x, nodoActual1.y)
        if item1 == "Diagonal":
            nodoActual1 = actualizaNodo(nodoActual1.x + nodoActual1.dx, nodoActual1.y + nodoActual1.dy, nodos)
            turtle1.goto(nodoActual1.x, nodoActual1.y)
        if item1 == "Horizontal":
            nodoActual1 = actualizaNodo(nodoActual1.x + nodoActual1.h, nodoActual1.y, nodos)
            turtle1.goto(nodoActual1.x, nodoActual1.y)
        turtle1.dot(20, "blue")

    turtle1.dot(20, "red")

def animaciont2(camino2, turtle2, nodos, nodoActual2):
    for item2 in camino2:        
        turtle2.speed(2)

        if item2 == "Salto":
            turtle2.goto(nodoActual2.x, nodoActual2.y + 100)
            nodoActual2 = actualizaNodo(nodoActual2.x + nodoActual2.a, nodoActual2.y, nodos)
            turtle2.goto(nodoActual2.x, nodoActual2.y + 100)
            turtle2.goto(nodoActual2.x, nodoActual2.y)
        if item2 == "Vertical":
            nodoActual2 = actualizaNodo(nodoActual2.x, nodoActual2.y + nodoActual2.v, nodos)
            turtle2.goto(nodoActual2.x, nodoActual2.y)
        if item2 == "Diagonal":
            nodoActual2 = actualizaNodo(nodoActual2.x + nodoActual2.dx, nodoActual2.y + nodoActual2.dy, nodos)
            turtle2.goto(nodoActual2.x, nodoActual2.y)
        if item2 == "Horizontal":
            nodoActual2 = actualizaNodo(nodoActual2.x + nodoActual2.h, nodoActual2.y, nodos)
            turtle2.goto(nodoActual2.x, nodoActual2.y)
        turtle2.dot(20, "green")

    turtle2.dot(20, "red")

def actualizaNodo(x, y, nodos):
    for n in nodos:
        if x == n.x and y == n.y: return n
    return -1

        
def determinarRuta(binario):
    ruta = []
    for i in range(len(binario)):
        if binario[i] == '1':
            if(i) == 0:
                ruta.append("Salto")
            if(i) == 1:
                ruta.append("Vertical")
            if(i) == 2:
                ruta.append("Diagonal")
            if(i) == 3:
                ruta.append("Horizontal")
    return ruta


def regresa(n):
    up()
    goto(n.x, n.y)
    down()

def limpiar():
    entradae1.delete(0, 'end')
    entradad1.delete(0, 'end')
    entradae2.delete(0, 'end')
    entradad2.delete(0, 'end')
    turtle.clearscreen()

ventana = Tk()
ventana.title("Hipercubo")
ventana.geometry('550x220')

ancho_ventana = ventana.winfo_reqwidth()
alto_ventana = ventana.winfo_reqheight()
posicion_x = int((ventana.winfo_screenwidth() / 2) - (ancho_ventana / 2))
posicion_y = int((ventana.winfo_screenheight() / 2) - (alto_ventana / 2) - 100)
ventana.geometry("+{}+{}".format(posicion_x, posicion_y))

#Entradas1
labelref1 = Label(ventana, text= "Ruta 1", background = "blue")
labelref1.grid(column = 2, row = 1, padx = (10,10), pady = (10,10))
emisor1= Label(ventana, text ="Emisor 1: ")
emisor1.grid(column = 2, row = 3, padx = (10,10), pady = (10,10))
entradae1 = Entry(ventana)
entradae1.grid(column = 4, row = 3, padx = (6,6), pady = (10,10))

destino1= Label(ventana, text ="Destino 1: ")
destino1.grid(column = 2, row = 5, padx = (10,10), pady = (10,10))
entradad1 = Entry(ventana)
entradad1.grid(column = 4, row = 5, padx = (6,6), pady = (10,10))

#Entradas2
labelref2 = Label(ventana, text= "Ruta 2", background = "green")
labelref2.grid(column = 6, row = 1, padx = (10,10), pady = (10,10))

emisor2= Label(ventana, text ="Emisor 2: ")
emisor2.grid(column = 6, row = 3, padx = (10,10), pady = (10,10))
entradae2 = Entry(ventana)
entradae2.grid(column = 8, row = 3, padx = (6,6), pady = (10,10))

destino2= Label(ventana, text ="Destino 2: ")
destino2.grid(column = 6, row = 5, padx = (10,10), pady = (10,10))
entradad2 = Entry(ventana)
entradad2.grid(column = 8, row = 5, padx = (6,6), pady = (10,10))


#Start
ingreso = Button(ventana, text = "Inicio", command = ruta )
ingreso.grid(column = 5, row = 7, padx = (30,30), pady = (10,10))
ventana.bind('<Return>', lambda event=None: ingreso.invoke())

boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(column = 5, row = 8, padx=(10, 10), pady=(10, 10))


ventana.mainloop()
