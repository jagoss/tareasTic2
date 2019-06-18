import json
import random

def truco():
    DICT_TRUCO = json.load(open('truco.json'))  # abre el archivo y lo carga en un diccionario Python

    mazo = DICT_TRUCO["Mazo"]
    jugadores = DICT_TRUCO["Jugadores"]
    palo = "palo"
    numero = 0
    muestra = ["palo", 0]

    #Repartir las cartas
    for i in range (0,3): #for para los 4 jugadores
        for j in range(0,2): #for para las 3 cartas de un jugador
            palo = random.choice(mazo)
            numero = random.choice(mazo[palo])
            (mazo[palo]).remove(numero) #suponemos que esto esta bien. No sabemos
            ((jugadores[i])[j])[0] = palo
            ((jugadores[i])[j])[1] = numero

    #elijo muestra
    palo = random.choice(mazo)
    numero = random.choice(mazo[palo])
    (mazo[palo]).remove(numero)  # suponemos que esto esta bien. No sabemos
    muestra = [palo, numero]

    for i in range(0,3):
        print("El jugador " + i + "tiene las cartas: " + str(jugadores[i]))

        if(checkForFlor(jugadores[i]), muestra):
            print("FLOR de " + contarFlor(jugadores[i], muestra) + "puntos")
        else:
            print("ENVIDO de " + contarEnvido(jugadores[i], muestra) + "puntos")



def checkForFlor(player, muestra):
    nroPiezas=0
    piezas = [2,4,5,11,10]
    noPiezas = [0]*3
    contador = 0
    #chequear 3 palos iguales
    if ((player[0])[0]==(player[1])[0] and (player[0])[0]==(player[2])[0]):
        return True


    for i in range(0,2):
        if(muestra[0] == (player[i])[0] and ((player[i])[1] in piezas)):
            nroPiezas+=1
        else:
            noPiezas[contador] = player[i]
            contador+=1

    # chequar 2 muestras
    if(nroPiezas == 2):
        return True

    if(nroPiezas==1):
        if((noPiezas[0])[0] == (noPiezas[1])[0]):
            return True

    return False

def contarFlor(player, muestra):

def contarEnvido(player, muestra):