"""Conecta cuatro
Autor: Jesús Antonio Murcia
18-07-2024"""

from os import system

def leerOpcion():
    opcion = input("Ingrese la opción a jugar: ")
    while opcion not in "012" or opcion == '':
        opcion = input("ingrese una opción valida, intente otra vez: ")
    return int(opcion)

def crearTablero():
    tablero = [[ 0 for i in range(7)] for i in range(6)]
    return tablero

def mostrarTablero(tablero):
    for i in range(len(tablero)):
        for value in tablero[i]: #Iterar por cada fila
            print("x" if value == -1 else "o" if value == 1 else "-", end="|")
        print()#Salto de línea
    for i in range(len(tablero[0])):
        print(i+1, end=" ")#Para enumerar casillas
    print()

def pedirCasillaAMarcar(tablero):
    casillaValida = False
    posicion = input("Ingrese la casilla a marcar: ")
    while not casillaValida:
        if posicion in "1234567" and len(posicion) == 1:
            posicion = int(posicion) -1
            for i in range(6): #Verificar que la casilla no este llena
                if tablero[i][posicion] == 0:
                    casillaValida = True
                    break
        if not casillaValida:
            posicion = input("Ingrese una casilla valida, intente nuevamente: ")
    return posicion

def marcarTablero(tablero, posicion, jugador):
    for i in range(5, -1, -1):
        if tablero[i][posicion] == 0: #Revisar que la columna este vacia
            tablero[i][posicion] = jugador
            break
    return tablero

def empate(tablero): 
    empate = True
    for columna in tablero:
        if 0 in columna:
            empate = False
            break
    return empate

def victoria(tablero):
    ganador = None
    for i in range(len(tablero)):
        if tablero[i][3] != 0:#la cuarta posición de cada fila siempre es necesaria para una línea horizontal
            ganador = tablero[i][3]
            posicion = 3
            cantidad = 0

            while posicion >= 0 and tablero[i][posicion] == ganador: #Buscar desde donde empieza la línea horizontal
                posicion -= 1
            posicion += 1 #Restablecer valor donde empieza el patron

            while cantidad < 3 and tablero[i][posicion] == ganador:
                posicion += 1
                cantidad += 1
            if cantidad == 4:
                return ganador
            else:
                ganador = None
    return ganador
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
            jugador = 1
            while not empate(tablero) and victoria(tablero) == None:
                casilla = pedirCasillaAMarcar(tablero)
                tablero = marcarTablero(tablero, casilla, jugador)
                mostrarTablero(tablero)
                jugador*=-1
            if empate(tablero):
                print("Empate")
            else:
                print("victoria")

        case 2:
            print("juego individual")
        case 0:
            continuar = False
            print("Gracias por jugar")