import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import time
tantos = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R",]
palos=["monedas", "copas", "espadas", "bastos",] 
cartas_d = [] 
num_car = 40

def generar_cartas():  


    print("SE ESTÁ CREANDO LA BARAJA ...\n")
    print(45*"☺")
    for v in range(len(tantos)):

        for s in range(len(palos)):
            #card = tantos[v]+str(" de ")+palos[s]+"\t"
            card = palos[s] + tantos[v]
            cartas_d.append(card)
            img = mpimg.imread("./" + card + ".gif")

            plt.imshow(img)
            plt.show()

    return cartas_d


class Carta():
    def __init__(self,palo,num): 
        self.palo = palo
        self.num   = num
    def mostrar_carta(self): 
        print('{} de {}'.format(self.palo, self.num))

class deck_Baraja(): #DeckOfCards
    def __init__(self):
        print("Se mostrará en texto la baraja ...")
        cartas_n = [Carta(palo,num) for palo in range(1,1) for num in tantos] 
        cara_carta = [Carta(palo,num) for palo in palos for num in tantos] 
        self.baraja_cartas = cartas_n+cara_carta  
        #assert len(self.baraja_cartas) == num_car #

    def mostrar_baraja(self): #show_deck
        for carta in self.baraja_cartas:
            carta.mostrar_carta()

    def revolver_baraja(self):  #suffle_deck
         print(80*'-')
         print("se están barajeando las cartas ")
         print(80*'-')
         random.shuffle(self.baraja_cartas)
         
         
    def revolver_baraja_mostrar(self):
        print('se van a mostrar las cartas revueltas')
        random.shuffle(card)
        print(card)
        
    def dar_carta(self): #draw_card
        #x = int(input('Ingresa cuantas cartas quieres repartir'))
        print("Se está repartiendo")
        return self.baraja_cartas.pop()

class Jugador():
    def __init__(self, jugador_nombre= '1'):
        self.jugador_nombre = jugador_nombre
        self.jugador_mano = [] #player_hand

    def repartir_carta(self,baraja): #draw_card
        print("Jugador {} se le reparte la carta ".format(self.jugador_nombre))
        self.jugador_mano.append(baraja.dar_carta())
        return self
    def mostrar_mano(self): #show_hand
        print("Mostrando las cartas de la mano ")
        for card in self.jugador_mano:
            card.mostrar_carta()
            
if __name__ ==  '__main__':
    
    def menu():
        while True:
            print (50*'♥')
            op = input('Introduce la opcion deseada')
            if op =='1':
                deck=generar_cartas()
                d = deck_Baraja()
                d.mostrar_baraja()
            elif op == '2':
                
                d = deck_Baraja()
                d.revolver_baraja()
                d.mostrar_baraja()
                
            elif op =='3':
                print(5*'☻☺')
                J1=input('Elige El nombre del primer Jugador :')
                print(5*'☻☺')
                J4= input('Elige el nombre del segundo Jugador :')
                J2 = Jugador(J1)
                J2.repartir_carta(d).repartir_carta(d).repartir_carta(d).repartir_carta(d) #Se le agregan las cartas al Jugador 
                J2.mostrar_mano()
                J3 = Jugador(J4)
                print(J3)
                ret = J3.repartir_carta(d).repartir_carta(d).repartir_carta(d)
                print(ret)
                print(J3 is ret)
                J3.mostrar_mano()
            elif op == '4':
                print('\nlas cartas faltantes son :', len(d.baraja_cartas))
            
            elif op=='5':
                print('Vas a salir del programa')
                break
            
            else :
                print('Solo puedes elegir numeros')
                print (50*'♥')
                print ('Vuelve a Interntarlo')
                
                

print ('***********************Proyecto Intersemestral****************************')
print('Estas son las opciones')
print('1 =  Mostrar Cartas')             
print('2 =  Barajear Cartas')    
print('3 =  Repartir Cartas')
print('4 =  Mostrar Cartas Faltantes')            
print('5 =  Salir')
menu()     
#    deck=generar_cartas() 
#    d = deck_Baraja()
#    d.mostrar_baraja()
#    d.revolver_baraja()
#    d.mostrar_baraja()
#    print()
#    Jugador1 = Jugador('Edgar')
#    Jugador1.repartir_carta(d).repartir_carta(d).repartir_carta(d)
#    Jugador1.mostrar_mano()
#    Jugador2 = Jugador('Salma')
#    print(Jugador2)
#    ret = Jugador2.repartir_carta(d).repartir_carta(d)
#    print(ret)
#    print(Jugador2 is ret)
#    Jugador2.mostrar_mano()
#    print('\nlas cartas faltantes son :', len(d.baraja_cartas))
