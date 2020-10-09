import random
def imprimir_tablero (x):
    for fila in x:
        print()
        print()
        for elemento in fila:
            print(f"|{elemento}|", end="")

def rellenar_tablero (lista, tablero, jugador):
    if jugador == "X":
        tablero[lista[0]][lista[1]]= "X"
    elif jugador == "O":
        tablero[lista[0]][lista[1]]= "O"
    return tablero

def ganador(tablero):
    fil = 0
    col = 0
    gan = False
    while fil < 3 and gan == False:
        if tablero[fil][0] == "X" and tablero[fil][1] == "X" and tablero[fil][2] == "X":
            print()
            print("¡Ganó el jugador 1!")
            gan = True
            break
        elif tablero[fil][0] == "O" and tablero[fil][1] == "O" and tablero[fil][2] == "O":
            print()
            print("¡Ganó el jugador 2!")
            gan = True
            break
        fil += 1
    while col < 3 and gan == False:
        if tablero[0][col] == "X" and tablero[1][col] == "X" and tablero[2][col] == "X":
            print()
            print("¡Ganó el jugador 1!")
            gan = True
            break
        elif tablero[0][col] == "O" and tablero[1][col] == "O" and tablero[2][col] == "O":
            print()
            print("¡Ganó el jugador 2!")
            gan = True
            break
        col += 1
    contador = 0
    while contador < 3 and gan == False:
        if tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X":
            print()
            print("¡Ganó el jugador 1!")
            gan = True
            break
        elif tablero[0][0] == "O" and tablero[1][1] == "O" and tablero[2][2] == "O":
            print()
            print("¡Ganó el jugador 2!")
            gan = True
            break
        elif tablero[2][0] == "X" and tablero[1][1] == "X" and tablero[0][2] == "X":
            print()
            print("¡Ganó el jugador 1!")
            gan = True
            break
        elif tablero[2][0] == "O" and tablero[1][1] == "O" and tablero[0][2] == "O":
            print()
            print("¡Ganó el jugador 2!")
            gan = True
            break
        contador += 3
    return gan     

#Programa principal
tablero = [["_"]*3 for i in range (3)]
print("TA-TE-TI")
imprimir_tablero(tablero)
print()
print()
modo = input("¿Desea jugar solo o con un compañero? ")
jugadas_hechas = 0
tablero_ocupado = []
if modo.strip().lower() == "solo":
    print("Usted jugará en solitario contra la maquina.")
    print("Para indicar una coordenada debe ingresar dos números entre 0 y 2.")
    jugador1 = input("Elija 'X' o 'O': ").upper()
    if jugador1 == "X":
        jugador2 = "O"
    elif jugador1 == "O":
        jugador2 = "X"
    while jugadas_hechas < 9:
        print()
        print()
        #CUANDO EL USUARIO ELIJE X
        if jugador1 == "X":
            #JUGADA DEL JUGADOR X
            if jugadas_hechas < 9:
                print("Turno del jugador 1.")
                jugada_fil = int(input("¿En que fila desea poner su 'X'? "))
                jugada_col = int(input("¿En que columna desea poner su 'X'? "))
                jugada = [jugada_fil, jugada_col]
                while True:
                    if jugada not in tablero_ocupado:
                        break
                    elif jugada in tablero_ocupado:
                        jugada_fil = int(input("Esa posición está ocupada. Ingrese otra fila:  "))
                        jugada_col = int(input("Ingrese otra columna:  "))
                        jugada = [jugada_fil, jugada_col]
                tablero_ocupado.append(jugada)
                imprimir_tablero(rellenar_tablero(jugada, tablero, jugador1))
                jugadas_hechas += 1
                if jugadas_hechas >= 5:
                    final = ganador(tablero)
                    if final == True:
                        break
                    else:
                        continue
            #JUGADA DEL JUGADOR O (MAQUINA)
            if jugadas_hechas < 9:
                print()
                print()
                print("Turno del jugador 2.")
                jugada_fil = random.randint(0,2)
                jugada_col = random.randint(0,2)
                jugada = [jugada_fil, jugada_col]
                while True:
                    if jugada not in tablero_ocupado:
                        break
                    elif jugada in tablero_ocupado:
                        jugada_fil = random.randint(0,2)
                        jugada_col = random.randint(0,2)
                        jugada = [jugada_fil, jugada_col]
                tablero_ocupado.append(jugada)
                imprimir_tablero(rellenar_tablero(jugada, tablero, jugador2))
                jugadas_hechas += 1
                if jugadas_hechas >= 5:
                    final = ganador(tablero)
                    if final == True:
                        break
                    else:
                        continue
        final = ganador(tablero)
        if final == False:
        print("¡Empate!")
        #CUANDO EL USUARIO ELIJE O
        elif jugador1 == "O":
            #JUGADA DEL JUGADOR  X (MAQUINA)
            if jugadas_hechas < 9:
                print()
                print()
                print("Turno del jugador 1.")
                jugada_fil = random.randint(0,2)
                jugada_col = random.randint(0,2)
                jugada = [jugada_fil, jugada_col]
                while True:
                    if jugada not in tablero_ocupado:
                        break
                    elif jugada in tablero_ocupado:
                        jugada_fil = random.randint(0,2)
                        jugada_col = random.randint(0,2)
                        jugada = [jugada_fil, jugada_col]
                tablero_ocupado.append(jugada)
                imprimir_tablero(rellenar_tablero(jugada, tablero, jugador2))
                jugadas_hechas += 1
                if jugadas_hechas >= 5:
                    final = ganador(tablero)
                    if final == True:
                        break
                    else:
                        continue
    final = ganador(tablero)
    if final == False:
            #JUGADA DEL JUGADOR O
            if jugadas_hechas < 9:
                print()
                print()
                print("Turno del jugador 2.")
                jugada_fil = int(input("¿En que fila desea poner su 'O'? "))
                jugada_col = int(input("¿En que columna desea poner su 'O'? "))
                jugada = [jugada_fil, jugada_col]
                while True:
                    if jugada not in tablero_ocupado:
                        break
                    elif jugada in tablero_ocupado:
                        jugada_fil = int(input("Esa posición está ocupada. Ingrese otra fila:  "))
                        jugada_col = int(input("Ingrese otra columna:  "))
                        jugada = [jugada_fil, jugada_col]
                tablero_ocupado.append(jugada)
                imprimir_tablero(rellenar_tablero(jugada, tablero, jugador1))
                jugadas_hechas += 1
                if jugadas_hechas >= 5:
                    final = ganador(tablero)
                    if final == True:
                        break
                    else:
                        continue
        
else:
    print("Usted jugará contra un compañero.")
    print("Para indicar una coordenada debe ingresar dos números separados por una coma.")
    jugador1 = input("Elija 'X' o 'O': ").upper()
    if jugador1 == "X":
        jugador2 = "O"
    elif jugador1 == "O":
        jugador2 = "X"
    while jugadas_hechas < 9:
        print()
        print()
        #JUGADA DEL JUGADOR X
        if jugadas_hechas < 9:
            print("Turno del jugador 1.")
            jugada_fil = int(input("¿En que fila desea poner su 'X'? "))
            jugada_col = int(input("¿En que columna desea poner su 'X'? "))
            jugada = [jugada_fil, jugada_col]
            while True:
                if jugada not in tablero_ocupado:
                    break
                elif jugada in tablero_ocupado:
                    jugada_fil = int(input("Esa posición está ocupada. Ingrese otra fila:  "))
                    jugada_col = int(input("Ingrese otra columna:  "))
                    jugada = [jugada_fil, jugada_col]
            tablero_ocupado.append(jugada)
            imprimir_tablero(rellenar_tablero(jugada, tablero, jugador1))
            jugadas_hechas += 1
            if jugadas_hechas >= 5:
                final = ganador(tablero)
                if final == True:
                    break
                else:
                    pass
        if jugadas_hechas < 9:
            print()
            print()
            print("Turno del jugador 2.")
            jugada_fil = int(input("¿En que fila desea poner su 'O'? "))
            jugada_col = int(input("¿En que columna desea poner su 'O'? "))
            jugada = [jugada_fil, jugada_col]
            while True:
                if jugada not in tablero_ocupado:
                    break
                elif jugada in tablero_ocupado:
                    jugada_fil = int(input("Esa posición está ocupada. Ingrese otra fila:  "))
                    jugada_col = int(input("Ingrese otra columna:  "))
                    jugada = [jugada_fil, jugada_col]
            tablero_ocupado.append(jugada)
            imprimir_tablero(rellenar_tablero(jugada, tablero, jugador2))
            jugadas_hechas += 1
            if jugadas_hechas >= 5:
                final = ganador(tablero)
                if final == True:
                    break
                else:
                    continue