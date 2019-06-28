import random

def truco():

    DICT_TRUCO = {
    "Mazo": {
        "Oro": [1,2,3,4,5,6,7,10,11,12],
        "Basto": [1,2,3,4,5,6,7,10,11,12],
        "Copa": [1,2,3,4,5,6,7,10,11,12],
        "Espada": [1,2,3,4,5,6,7,10,11,12]
    },
    "Jugadores": {
        "0": [["palo",0],["palo",0],["palo",0]],
        "1": [["palo",0],["palo",0],["palo",0]],
        "2": [["palo",0],["palo",0],["palo",0]],
        "3": [["palo",0],["palo",0],["palo",0]]
    },
    "Puntajes":{
        "Piezas":[[2,30],[4,29],[5,28],[11,27],[10,27]],
        "Blancas y Negras": [ [1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,0],[9,0],[10,0],[11,0],[12,0] ]
    }
}

    mazo = DICT_TRUCO["Mazo"]
    jugadores = DICT_TRUCO["Jugadores"]
    puntajes = DICT_TRUCO["Puntajes"]
    numero = 0
    muestra = ["palo", 0]

    # Repartir las cartas
    for i in range (0,4): #for para los 4 jugadores
        for j in range(0,3): #for para las 3 cartas de un jugador
            palo = random.choice(["Oro", "Basto", "Copa", "Espada"])
            numero = random.choice(mazo[palo])
            (mazo[palo]).remove(numero) #suponemos que esto esta bien. No sabemos
            istring = str(i)
            jug = jugadores[istring]
            carta = jug[j]
            (carta)[0] = palo
            (carta)[1] = numero

    # elijo muestra
    palo = random.choice(["Oro", "Basto", "Copa", "Espada"])
    numero = random.choice(mazo[palo])
    (mazo[palo]).remove(numero)  # suponemos que esto esta bien. No sabemos
    muestra = [palo, numero]

    piezas = [2,4,5,11,10]
    # sustituir el 12 si salio una pieza de muestra
    for i in range(len(piezas)):
        if (muestra[1] == piezas[i]):
            piezas[i] = 12
            for i in range (len(puntajes["Piezas"])):
                if(((puntajes["Piezas"])[i])[0] == muestra[1]):
                    ((puntajes["Piezas"])[i])[0] = 12

    print("La muestra es de " + str(muestra))
    for i in range(0,3):
        print("El jugador " + str(i) + " tiene las cartas: " + str(jugadores[str(i)]))
        if(checkForFlor(jugadores[str(i)], muestra, piezas)):
            puntos_flor = contarFlor(jugadores[str(i)], muestra, puntajes, piezas)
            print("FLOR de " + str(puntos_flor) + " puntos")
        else:
            puntos_envido = contarEnvido(jugadores[str(i)], muestra, puntajes, piezas)
            print("ENVIDO de " + str(puntos_envido) + " puntos")

def checkForFlor(player, muestra, piezas):
    nroPiezas=0
    noPiezas = [0]*3
    contador = 0
    #chequear 3 palos iguales
    if ((player[0])[0]==(player[1])[0] and (player[0])[0]==(player[2])[0]):
        return True

    for i in range(0,3):
        if(muestra[0] == (player[i])[0] and ((player[i])[1] in piezas)):
            nroPiezas+=1
        else:
            noPiezas[contador] = player[i]
            contador+=1

    # chequar 2 piezas
    if(nroPiezas == 2):
        return True

    #chequar 1 pieza y dos iguales
    if(nroPiezas==1):
        if((noPiezas[0])[0] == (noPiezas[1])[0]):
            return True

    return False

def contarFlor(player, muestra, puntajes, piezas):
    scores = [0,0,0]
    puntajesPiezas = puntajes['Piezas']
    puntajesNormales = puntajes['Blancas y Negras']

    # hallar los puntajes de cada carta.
    for i in range(0,3):
        # ver si es una pieza
        if (muestra[0] == (player[i])[0] and ((player[i])[1] in piezas)):
            #buscar puntaje de la pieza
            for j in range(len(puntajesPiezas)):
                    #guardar puntaje de pieza
                    if((puntajesPiezas[j])[0] == player[i][1]):
                        scores[i] = (puntajesPiezas[j])[1]
        else:
            #guardar puntaje de carta que no es pieza
            nro_i_carta = player[i][1]
            if nro_i_carta >= 10:
                nro_i_carta -= 3
            scores[i] = (puntajesNormales[nro_i_carta - 1])[1]
    # ordenarlos
    scores.sort(reverse=True)
    # quedarme con el primero pero entero
    puntajeTotal = scores[0]
    # hacer el %10 de los otros 2 y sumarlos
    puntajeTotal += scores[1]%10
    puntajeTotal += scores[2]%10

    return puntajeTotal

def hallarCasoEnvido(player, muestra, piezas):
    for i in range(0, 3):
        if (muestra[0] == (player[i])[0] and ((player[i])[1] in piezas)):
            # caso 1 (una pieza en la posicion i)
            caso = [1,i,0]
            return caso
    if((player[0])[0] == (player[1])[0]):
        # dos cartas del mismo palo en posicion 0 y 1
        caso = [2, 0, 1]
        return caso
    elif ((player[0])[0] == (player[2])[0]):
        # dos cartas del mismo palo en posicion 0 y 2
        caso = [2, 0, 2]
        return caso
    elif ((player[1])[0] == (player[2])[0]):
        # dos cartas del mismo palo en posicion 1 y 2
        caso = [2, 1, 2]
        return caso
    else:
        # todas las cartas de diferentes palos
        caso = [3, 0, 0]
        return caso

def contarEnvido(player, muestra, puntajes, piezas):
    puntajeEnvido = 0
    puntajesPiezas = puntajes["Piezas"]
    puntajesNormales = puntajes["Blancas y Negras"]
    # tres casos
    caso = hallarCasoEnvido(player, muestra, piezas)

    # caso 1: 1 pieza
    if caso[0] == 1:
        miPieza = caso[1]
        for i in range(0, 3):
            nro_i_carta = player[i][1]
            if ((puntajesNormales[nro_i_carta - 1][1] >= puntajeEnvido) and (miPieza != i)):
                puntajeEnvido = puntajesNormales[nro_i_carta - 1][1]
        nro_mi_pieza = player[caso[1]][1]
        for x in puntajesPiezas:
            if x[0] == nro_mi_pieza:
                puntajeEnvido += x[1]

    # caso 2: 2 palos iguales
    elif (caso[0] == 2):
        nro_primer_carta = player[caso[1]][1]
        nro_segunda_carta = player[caso[2]][1]
        puntajeEnvido = 20 + puntajesNormales[nro_primer_carta - 1][1] + puntajesNormales[nro_segunda_carta - 1][1]

    # caso 3: los 3 palos diferentes
    elif (caso[0] == 3):
        nro_primer_carta = player[0][1]
        nro_segunda_carta = player[1][1]
        nro_tercer_carta = player[2][1]
        puntajeEnvido = max(puntajesNormales[nro_primer_carta - 1][1], puntajesNormales[nro_segunda_carta - 1][1], puntajesNormales[nro_tercer_carta - 1][1])

    return puntajeEnvido

def main():
    truco()

if __name__ == '__main__':
    main()




