RIGHE = 3
COLONNE = 3

def print_campo(campo):
    print(" "*8, "Col. 0 Col. 1 Col. 2")
    for i in range(RIGHE):
        print("Riga %d" %i, end="")
        for j in range(COLONNE):
            print("%7s" %campo[i][j], end="")
        print()

def occupata(campo,coordinate):
    return campo[int(coordinate[0])][int(coordinate[1])] != "-"

def main():
    tris = [["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]
    
    print_campo(tris)
    turno = 1
    vinto = False
    finito= False

    while not vinto and not finito:
        if turno == 1:
            valida = False
            while not valida:
                mossaPlayer1 = input("Giocatore1 riga e colonna: ")
                coordinate = mossaPlayer1.split()
                valida = not occupata(tris,coordinate)
                if not valida:
                    print("Casella già occupata")
            tris[int(coordinate[0])][int(coordinate[1])] = "X"
            print_campo(tris)

if  __name__ == "__main__":
    main()