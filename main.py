"""Conecta cuatro
Autor: Jesús Antonio Murcia
18-07-2024"""

from os import system

def leerOpcion():
    opcion = input("Ingrese la opción a jugar: ")
    while opcion not in "012":
        opcion = input("ingrese una opción valida")
    return int(opcion)

def crearTablero():
    tablero = [[ 0 for i in range(6)] for i in range(6)]
    return tablero

def mostrarTablero(tablero):
    for i in range(len(tablero)):
        for value in tablero[i]: #Iterar por cada fila
            print("x" if value == -1 else "o" if value == 1 else " ", end=" ")
        print()#Salto de línea
    for i in range(len(tablero)):
        print(i+1, end=" ")#Para enumerar casillas

print("Bienvenido, jugemos conecta cuatro")
system("pause")
system("cls")

continuar = True
while continuar:
    print("\t\tMenú de opciones\n1.Jugar con dos personas \n2. Juego individual \n\t 0.Salir")
    opcion = leerOpcion()
    system("cls")
    tablero = crearTablero()
    mostrarTablero(tablero)
    match(opcion):
        case 1:
            print("Jugar con dos personas")
        case 2:
            print("juego individual")
        case 0:
            continuar = False
            print("Gracias por jugar")