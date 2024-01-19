import random, sys

def main():
    print("\nElige lo que quieres jugar: \n1. Piedra\n2. Papel\n3. Tijera")
    select = int(input("Ingresa el numero de tu eleccion:"))
    Ronda(select)

def VS(user,pc):
    if user == 1:
        user = "Piedra"
    elif user == 2:
        user = "Papel"
    elif user == 3:
        user = "Tijeras"
    
    if pc == 1:
        pc = "Piedra"
    elif pc == 2:
        pc = "Papel"
    elif pc == 3:
        pc = "Tijeras"

    print(user, " vs ", pc)
    

def Repeat():
    print("\nQuieres jugar otra vez?")
    print("1. Si\n2. No")
    rep = int(input("Ingresa el numero de la accion a realizar: "))
    if rep == 1:
        main()
    else:
        sys.exit()

def Ronda(sel):
    pc_selec=random.randint(1, 3)
    VS(sel, pc_selec)
    if sel == 1 and pc_selec == 1:
        print("Empate")
        Repeat()
    elif sel == 2 and pc_selec == 2:
        print("Empate")
        Repeat()
    elif sel == 3 and pc_selec == 3:
        print("Empate")
        Repeat()
    elif sel == 1 and pc_selec == 2:
        print("Has perdido, gana el papel.")
        Repeat()
    elif sel == 1 and pc_selec == 3:
        print("Has ganado, gana la piedra")
        Repeat()
    elif sel == 2 and pc_selec == 1:
        print("Has ganado, gana el papel")
        Repeat()
    elif sel == 2 and pc_selec == 3:
        print("Has perdido, ganan las tijeras")
        Repeat()
    elif sel == 3 and pc_selec == 1:
        print("Has perdido, gana la piedra")
        Repeat()
    elif sel == 3 and pc_selec == 2:
        print("Has ganado, ganan las tijeras")
        Repeat()


if __name__ == "__main__":
    main()
