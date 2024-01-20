import curses
import filecontent as f
import random


#DECK--------------------------------------------------------------------------------------

#Set cards and suits
suits = ['♣','♦','♥','♠'] # Clubs, Diamons, Hearts, Spades
base_cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_card(deck):
    return deck.pop(0)


#metodo nuevo-.---------------------------------------------------------------------------

def print_card(stdscr,num1,num2,string):
    stdscr.addstr(num1,num2,string)
    stdscr.refresh()
    stdscr.getch()

def change_icon(stdscr, carta, palo):
    stdscr.addstr(17,9,carta)
    stdscr.addstr(19,12,palo)
    stdscr.addstr(21,15,carta)
    stdscr.addstr(17,9,carta)
    stdscr.addstr(19,12,palo)
    stdscr.addstr(21,15,carta)
    stdscr.refresh()
    stdscr.getch()

def get_card(array):
    posicion = random.choice(range(len(array)))   
    elemento = array[posicion]
    return elemento

def valor_cartas(num1, num2):
    n1=0
    n2=0
    if num1 == '2':
        n1 = 2
    elif num1 == '3':
        n1 = 3
    elif num1 == '4':
        n1 = 4
    elif num1 == '5':
        n1 = 5
    elif num1 == '6':
        n1 = 6    
    elif num1 == '7':
        n1 = 7
    elif num1 == '8':
        n1 = 8
    elif num1 == '9':
        n1 = 9
    elif num1 == '10':
        n1 = 10
    elif num1  == 'J':
        n1 = 10
    elif num1  == 'Q':
        n1 = 10
    elif num1  == 'K':
        n1 = 10
    elif num1  == 'A':
        n1 = 11
    
    if num2 == '2':
        n2 = 2
    elif num2 == '3':
        n2 = 3
    elif num2 == '4':
        n1 = 4
    elif num1 == '5':
        n2 = 5
    elif num2 == '6':
        n2 = 6    
    elif num2 == '7':
        n2 = 7
    elif num2 == '8':
        n2 = 8
    elif num2 == '9':
        n2 = 9
    elif num2 == '10':
        n2 = 10
    elif num2  == 'J':
        n2 = 10
    elif num2  == 'Q':
        n2 = 10
    elif num2  == 'K':
        n2 = 10
    elif num2  == 'A':
        n2 = 11
    
    suma = n1 + n2

    return suma


def resultado(jug, ban):
    
    if jug > 21:
        frase = "Has perdido. Gana la banca, te has pasado de 21."
    elif ban > 21:
        frase = "Has ganado. Pierde la banca, se ha pasado de 21."
    elif jug > ban:
        frase ="Has ganado. Tu mano es mayor que la de la banca."
    elif jug< ban:
        frase ="Has perdido. Tu mano es menor que la de la banca."
    else:
        frase ="Empate. Tu mano es igual que la de la banca."

    return frase

def pedircarta(stdscr):
    stdscr.addstr(13,30,"Quieres otra carta?")
    cartanueva = input(stdscr.addstr(14,32,"1.Si      2.No"))
    



def game(stdscr,screen):
    stdscr.addstr(28,5, "                                                      ")
    stdscr.addstr(25,23,"      ")
    stdscr.addstr(25,48,"         ")
    #Se imprimen las cartas banca
    stdscr.addstr(3,8,"Mano Banca: ")
    stdscr.addstr(4,8," -------")
    stdscr.addstr(5,8,"|?      |")
    stdscr.addstr(6,8,"|       |")
    stdscr.addstr(7,8,"|   ?   |")
    stdscr.addstr(8,8,"|       |")
    stdscr.addstr(9,8,"|      ?|")
    stdscr.addstr(10,8," -------")
    
    stdscr.addstr(4,19," -------")
    stdscr.addstr(5,19,"|?      |")
    stdscr.addstr(6,19,"|       |")
    stdscr.addstr(7,19,"|   ?   |")
    stdscr.addstr(8,19,"|       |")
    stdscr.addstr(9,19,"|      ?|")
    stdscr.addstr(10,19," -------")
    #screen.refresh()
    #screen.getch()

    #Se imprimen las cartas jugador
    stdscr.addstr(15,8,"Mano jugador: ")
    stdscr.addstr(16,8," -------")
    stdscr.addstr(17,8,"|?      |")
    stdscr.addstr(18,8,"|       |")
    stdscr.addstr(19,8,"|   ?   |")
    stdscr.addstr(20,8,"|       |")
    stdscr.addstr(21,8,"|      ?|")
    stdscr.addstr(22,8," -------")
    
    stdscr.addstr(16,19," -------")
    stdscr.addstr(17,19,"|?      |")
    stdscr.addstr(18,19,"|       |")
    stdscr.addstr(19,19,"|   ?   |")
    stdscr.addstr(20,19,"|       |")
    stdscr.addstr(21,19,"|      ?|")
    stdscr.addstr(22,19," -------")
    screen.refresh()
    screen.getch()

    #cartas aleatorias jugador

    jugcarta1 = get_card(base_cards)
    jugpalo1 = get_card(suits)

    jugcarta2 = get_card(base_cards)
    jugpalo2 = get_card(suits)
    
    jugcarta3 = get_card(base_cards)
    jugpalo3 = get_card(suits)

    jugcarta4 = get_card(base_cards)
    jugpalo4 = get_card(suits)
    
    #cartas aleatorias banca

    bancarta1 = get_card(base_cards)
    banpalo1 = get_card(suits)

    bancarta2 = get_card(base_cards)
    banpalo2 = get_card(suits)
    
    bancarta3 = get_card(base_cards)
    banpalo3 = get_card(suits)

    bancarta4 = get_card(base_cards)
    banpalo4 = get_card(suits)

    #sumo las cartas

    jugsum1 = valor_cartas(jugcarta1, jugcarta2)
    jugsum2 = valor_cartas(jugcarta3, jugsum1)
    jugsum3 = valor_cartas(jugcarta4, jugsum2)
    
    bansum1 = valor_cartas(bancarta1, bancarta2)
    bansum2 = valor_cartas(bancarta3, bansum1)
    bansum3 = valor_cartas(bancarta4, bansum2)

    # pinto las cartas
    stdscr.addstr(17,9,jugcarta1)
    stdscr.addstr(19,12,jugpalo1)
    stdscr.addstr(21,15,jugcarta1)
    stdscr.addstr(17,20,jugcarta2)
    stdscr.addstr(19,23,jugpalo2)
    stdscr.addstr(21,26,jugcarta2)
    stdscr.addstr(25,5,"Valor de tu mano: ")
    stdscr.addstr(25,23,str(jugsum1))

    stdscr.addstr(5,20,bancarta2)
    stdscr.addstr(7,23,banpalo2)
    stdscr.addstr(9,26,bancarta2)
    screen.refresh()
    screen.getch()
    
    stdscr.addstr(5,9,bancarta1)
    stdscr.addstr(7,12,banpalo1)
    stdscr.addstr(9,15,bancarta1)
    stdscr.addstr(25,30,"Valor mano banca: ")
    stdscr.addstr(25,48,str(bansum1))


    pedircarta(stdscr)



    stdscr.addstr(28,5, resultado(jugsum1, bansum1))
    screen.refresh()
    screen.getch()

#MAIN------------------------------------------------------------------------------------------------
def main(stdscr):
    screen = curses.initscr()
    screen.refresh()
    curses.curs_set(0)
    screenheight, screenwidth = screen.getmaxyx()
    height, width = stdscr.getmaxyx()
    options = curses.newwin(screenheight, screenwidth, 0, 0)
    options.keypad(1)
    options.timeout(100)

    # Set the file name you want to display
    filename = 'BlackJack\plantilla.txt'
    # Call the function to print file content
    f.print_file_content(screen, filename)
    # Refresh the screen
    screen.refresh()
    stdscr.addstr(27,5,"Bienvenido a la mesa de Black, cuando estes preparado para jugar pulsa ·ESPACIO· ")
    screen.refresh()
    screen.getch()
    stdscr.addstr(27,5,"                                                                                       ")

    game(stdscr,screen)

    # Wait for user input
    while True:
        key = screen.getch()
        if key == 27:  # ASCII code for Escape key
            break
        else:
            game(stdscr,screen)



# Run the application
curses.wrapper(main)
