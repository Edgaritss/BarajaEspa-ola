#STEP 1
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def generar_cartas():  #generate_deck


    tantos = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R",] #values
    palos = ["monedas", "copas", "espadas", "bastos"] #suits
    cartas_d = [] #cards_deck

    for v in range(len(tantos)):

        for s in range(len(palos)):
            #card = tantos[v]+str(" de ")+palos[s]+"\t"
            card = palos[s] + tantos[v]
            cartas_d.append(card)
            img = mpimg.imread("./" + card + ".gif")
            plt.imshow(img)
            plt.show()

    return cartas_d



#STEP 2
def imprimir_d(completo): #print_deck

    print("La baraja es la siguiente")
    length = len(completo)
    cont= 0

    while cont!=length:
        print(deck[cont],"\t \t",deck[cont+1],"\t \t",deck[cont+2],"\t \t",deck[cont+3],"\t \t")
        cont += 4



#step 3:
def leer_jugador_nombre():

    nombres_list = [] #names_list
    print("Escribe el nombre de los 4 jugadores")

    for i in range(4):
        nombre = input("Ingresa el jugador "+str(i+1)+" nombre: ")
        nombres_list.append(nombre)

    return nombres_list



#step 4
def barajar_d(b_list): #shuffle_deck (deck_list)

    import random
    jugador_list = [] #player_card_list

    for i in range(10):
        carta_dar = random.choice(b_list) #card_drawn
        jugador_list.append(carta_dar)
        b_list.remove(carta_dar)


    return jugador_list

def mostrarCartasDisponibles(baraja):
    if baraja.verNumeroCartasRestantes(barajar_d) >= 1:
        cartas = baraja.mostrarCartas()
        print("Las cartas disponibles son:")
        imprimir_d(cartas)
    else:
        print("Ya no quedan cartas disponibles")

def darMuchasCartas(baraja, mano):
    numeroCartas = int(input("Escribe el número de cartas a repartir: "))
    if numeroCartas > baraja.verNumeroCartasRestantes():
        print("No hay suficientes cartas para repartir")
    else:
        for i in range(0, numeroCartas):
            barajar_d(baraja, mano)


#step 5
def imprimir_jugador_cartas(jugador1_cartas,jugador2_cartas,jugador3_cartas,jugador4_cartas,jugador_nom): #player1_cards,player2_cards,player3_cards,player4_cards,player_names
    x=int(input('Cuantas cartas quieres repartir'))
    if x > 11 :
        print("No hay cartas suficientes")
    else:
        print(jugador_nom[0],"cartas:\t \t \t",jugador_nom[1],"cartas:\t \t \t",jugador_nom[2],"cartas:\t \t \t",jugador_nom[3],"cartas:")
        for cont in range(x):
            print(jugador1_cartas[cont],"\t \t",jugador2_cartas[cont],"\t \t",jugador3_cartas[cont],"\t \t",jugador4_cartas[cont])
    print('se van a mostrar las cartas faltantes')

def menu():
    x = input('Elige la opcion deseada')
    if x == 1:
        imprimir_d()
    elif x == 2:
        darMuchasCartas()





###step 6


##step 7
menu()


# main program
print (25*"-_-")
print()


#Step 1:  Generating Deck
deck=generar_cartas()

#Step 2:  Printing Deck
imprimir_d(deck)
print (25*"---")
print()




#Step 3: Reading Players Names
jugador_nom=leer_jugador_nombre()
print (25*"---")
print()

#Step 4: Shuffling Deck
jugador1_cartas=barajar_d(deck)
jugador2_cartas=barajar_d(deck)
jugador3_cartas=barajar_d(deck)
jugador4_cartas=barajar_d(deck)

#Step 5: Printing Players Cards
imprimir_jugador_cartas(jugador1_cartas,jugador2_cartas,jugador3_cartas,jugador4_cartas,jugador_nom)
print (25*"---")


