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
            posicion += 1
            while cantidad < 4 and tablero[i][posicion] == ganador:
                posicion += 1
                cantidad += 1
            if cantidad == 4:
                return ganador
            
        #Revisar verticalmente, la columna no puede ser 6
        if i < 6 and tablero[2][i] != 0: #Si se ha ganado el tercer elemento de la fila debe estar marcado
            ganador = tablero[2][i]
            posicion = 2
            cantidad = 0

            #Revisar desde donde empieza
            while posicion < 6 and tablero[posicion][i] == ganador:#Se ejecuta hasta llegar a una posción inexistente o cuando no este el patron
                posicion += 1
            posicion-= 1 #Restaurar desde donde se inica
            while cantidad < 4 and tablero[posicion][i] == ganador: #Contar
                cantidad+= 1
                posicion -=1
            if cantidad == 4:
                return ganador
            
        #Diagonal
        posicionesVerticales = [
            [[5, 3]],
            [[4, 3], [0, 3]],
            [[3, 3], [1, 3]],
            [[3, 2], [3, 4]]
        ]
        for i in range(7):#Se analiza la columan con el indice dos, si esta marcada se accede a la otra posción escencial para la victoria diagonal
            if tablero[2][i] != 0:
                ganador = tablero[2][i]
                indice = i
                if i > 3:
                    indice = 6 - i
                #Comprobar las posiciones verticales
                for coordenadas in posicionesVerticales[indice]:
                    y = 2
                    x = i
                    if tablero[coordenadas[0]][coordenadas[1]] == ganador:
                        #Revisar la dirección, se determina desde la cordenada en la tercera columna

                        if coordenadas[0] > 2 and coordenadas[1] > i: #Dirección derecha-inferior
                            while x>= 0 and y >= 0 and tablero[y][x] == ganador: #Devolverse hasta donde inicia el patron
                                y-= 1
                                x-= 1
                            x+= 1 #Agregarle uno a las coordenadas para tener la coordenada de inicio
                            y+= 1
                            contador = 0
                            while contador < 4 and tablero[y][x] == ganador:
                                x+= 1
                                y+= 1
                                contador+= 1
                            if contador == 4:
                                return ganador
                        elif coordenadas[0] > 2 and coordenadas[1] < i: #Dirección izquierda-inferior
                            while x < 0 and y >= 0 and tablero[y][x] == ganador: #Devolverse hasta donde inicia el patron
                                y-= 1
                                x+= 1
                            x-= 1 #Agregarle uno a las coordenadas para tener la coordenada de inicio
                            y+= 1
                            contador = 0
                            while contador < 4 and y < 5 and x <= 0 and tablero[y][x] == ganador:
                                x-= 1
                                y+= 1
                                contador+= 1
                            if contador == 4:
                                return ganador
                        elif coordenadas[0] < 2 and coordenadas[1] > i:#Dirección derecha-superior
                            while x >= 0 and y < 6 and tablero[y][x] == ganador: #Devolverse hasta donde inicia el patron
                                y+= 1
                                x-= 1
                            x+= 1 #Agregarle uno a las coordenadas para tener la coordenada de inicio
                            y-= 1
                            contador = 0
                            while contador < 4 and tablero[y][x] == ganador:
                                x+= 1
                                y-= 1
                                contador+= 1
                            if contador == 4:
                                return ganador
                        else: #Diagonla izqueirda-superior
                            while x < 7 and y < 6 and tablero[y][x] == ganador: #Devolverse hasta donde inicia el patron
                                y+= 1
                                x+= 1
                            x-= 1 #Agregarle uno a las coordenadas para tener la coordenada de inicio
                            y-= 1
                            contador = 0
                            while contador < 4 and tablero[y][x] == ganador:
                                x-= 1
                                y-= 1
                                contador+= 1
                            if contador == 4:
                                return ganador
    return None

def puntuarTablero(tablero, jugador):
    if victoria(tablero):#Si hay victoria, la puntuación es la más alta
        return 1000 * jugador
    
    puntuacion= 0
    #Examinar posibles victorias
    #Horizontal
    for i in range(6): 
        contador = 0
        if tablero[i][3] != -jugador:
            contador += 1

            #Revisar casillas de la columna
            posicion = 3

            while posicion <= 0 and tablero[i][posicion] != -jugador:
                posicion -= 1
            posicion+= 1 #Restaurar inicio del patrón

            cantidad = 0 #Contar
            while cantidad < 4 and posicion < 6 and tablero[i][posicion] != -jugador:
                cantidad += 1
                posicion += 1
            puntuacion += cantidad**2 #Se eleva al cuadrado para que a mayor cantidad de espacios ocupados, tenga mayor importancia
        #Vertical
        if i < 6 and tablero[2][i] != -jugador:
            contador +=1

            #Revisar casillas de la fila
            posicion = 2
            while posicion < 6 and tablero[posicion][i] != -jugador:
                posicion += 1
            posicion -= 1

            cantidad = 0 #contar

            while cantidad < 4 and posicion < 5 and tablero[posicion][i] != -jugador:
                cantidad += 1
                posicion += 1
            
            puntuacion += cantidad**2 #Se eleva al cuadrado para que a mayor cantidad de espacios ocupados, tenga mayor importancia
        #Diagonal
        posicionesVerticales = [
            [[5, 3]],
            [[4, 3], [0, 3]],
            [[3, 3], [1, 3]],
            [[3, 2], [3, 4]]
        ]
        for i in range(7):#Se analiza la columan con el indice dos, si esta marcada se accede a la otra posción escencial para la victoria diagonal
            if tablero[2][i] != jugador*-1:
                indice = i
                if i > 3:
                    indice = 6 - i
                #Comprobar las posiciones verticales
                
                contador = 0
                for coordenadas in posicionesVerticales[indice]:
                    y = 2
                    x = i
                    if tablero[coordenadas[0]][coordenadas[1]] != jugador*-1:
                        #Revisar la dirección, se determina desde la cordenada en la tercera columna

                        if coordenadas[0] > 2 and coordenadas[1] > i: #Dirección derecha-inferior
                            while x>= 0 and y >= 0 and tablero[y][x] == jugador*-1: #Devolverse hasta donde inicia el patron
                                y-= 1
                                x-= 1
                            x+= 1 #Agregarle uno a las coordenadas para tener la coordenada de inicio
                            y+= 1
                            while contador < 4 and tablero[y][x] == jugador*-1:
                                x+= 1
                                y+= 1
                                contador+= 1
                        elif coordenadas[0] > 2 and coordenadas[1] < i: #Dirección izquierda-inferior
                            while x < 0 and y >= 0 and tablero[y][x] != jugador*-1: #Devolverse hasta donde inicia el patron
                                y-= 1
                                x+= 1
                            x-= 1 #Agregarle uno a las coordenadas para tener la coordenada de inicio
                            y+= 1
                            while contador < 4 and y < 5 and x <= 0 and tablero[y][x] != jugador*-1:
                                x-= 1
                                y+= 1
                                contador+= 1
                        elif coordenadas[0] < 2 and coordenadas[1] > i:#Dirección derecha-superior
                            while x >= 0 and y < 6 and tablero[y][x] != jugador*-1: #Devolverse hasta donde inicia el patron
                                y+= 1
                                x-= 1
                            x+= 1 #Agregarle uno a las coordenadas para tener la coordenada de inicio
                            y-= 1
                            while contador < 4 and tablero[y][x] != jugador*-1:
                                x+= 1
                                y-= 1
                                contador+= 1
                        else: #Diagonla izqueirda-superior
                            while x < 7 and y < 6 and tablero[y][x] != jugador*-1: #Devolverse hasta donde inicia el patron
                                y+= 1
                                x+= 1
                            x-= 1 #Agregarle uno a las coordenadas para tener la coordenada de inicio
                            y-= 1
                            while contador < 4 and tablero[y][x] != jugador*-1:
                                x-= 1
                                y-= 1
                                contador+= 1
                puntuacion += contador**2
    return puntuacion

def minMax(tableroInicial, jugador, iteracion = 0):
    tablero = tableroInicial[:]
    puntuacionYMovimientos = []
    if iteracion == 3 or victoria(tablero): #Limitar las iteraciones para salir de la función
        return [puntuarTablero(tablero, jugador)]
    else:
        for i in range(7): #Marcar posilbes movimientos
            tableroAux = tablero[:]
            tableroAux = marcarTablero(tableroAux, i, jugador) #No se marca si la columan esta llena
            puntuacion = minMax(tableroAux, jugador*-1, iteracion+ 1)
            puntuacionYMovimientos.append([puntuacion[0], i])
    print(puntuacionYMovimientos)
    puntuacionYMovimientos.sort(key = lambda x: x[0])#Retornar el mejor movimiento
    if jugador == -1:
        puntuacionYMovimientos.reverse()
    return puntuacionYMovimientos[0]



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
            jugador = -1
            while victoria(tablero) == None and not empate(tablero):
                tableroDePrueba = tablero[:]
                #print(minMax(tableroDePrueba, jugador)[1])
                casilla = pedirCasillaAMarcar(tablero)
                tablero = marcarTablero(tablero, casilla, jugador)
                mostrarTablero(tablero)
                print(f"La puntuacion para {"o" if jugador == 1 else "x"} es {puntuarTablero(tablero, jugador)}")
                jugador*=-1
            if empate(tablero):
                print("Empate")
            else:
                print(f"victoria, ganador: {"x" if victoria(tablero) == -1 else "o"}")

        case 2:
            print("juego individual")
        case 0:
            continuar = False
            print("Gracias por jugar")