#Memory
from random import randint
from time import sleep, time
import os
RIGHE   = 3
COLONNE = 3
TEMPO = max(COLONNE,RIGHE)//min(COLONNE,RIGHE) * min(COLONNE,RIGHE)

def print_campo(campo):
    for i in range(RIGHE):
        for j in range(COLONNE):
            print(campo[i][j], end=" ")
        print()

def riempi_campo(campo):
    Coppie_piene = COLONNE * RIGHE // 2
    caselle_vuote = COLONNE * RIGHE - Coppie_piene

    numeri = randint(1,Coppie_piene)


def main():

    table = [ [1,2,3],
              [3,7,5],
              [7,5,2]]
    # table = [["-"]* COLONNE] * RIGHE
    # empty_table = table.copy()
    empty_table = [["-"]* COLONNE] * RIGHE
    # print_campo(table)
    # os.system("cls")
    print()
    print_campo(empty_table)
    scelta = input("S per iniziare Q per uscire: ")
    if scelta.upper() == "S":
        punteggio = 0
        tempoInizio = time()
        os.system("cls")
        print()
        print_campo(table)
        sleep(TEMPO)
        os.system("cls")
        print_campo(empty_table)
        while punteggio <  COLONNE * RIGHE // 2:
            primo = input("Riga e colonna primo valore: ")
            cP = primo.split()
            secondo = input("Riga e colonna secondo valore: ")
            cS = secondo.split()

            if table[int(cP[0])][int(cP[1])] == table[int(cS[0])][int(cS[1])]:
                punteggio += 1
                # print(empty_table[int(cP[0])][int(cP[1])])
                # print(empty_table[int(cS[0])][int(cS[1])])
                # print(table[int(cP[0])][int(cP[1])])
                # print(table[int(cP[0])][int(cP[1])])

                empty_table[int(cP[0])][int(cP[1])] = table[int(cP[0])][int(cP[1])]
                empty_table[int(cS[0])][int(cS[1])] = table[int(cS[0])][int(cS[1])]
                # os.system("cls")
                print("BRAVOOOOOO!")

            else:
                print("COGLIONE AHAHAH")
            print_campo(empty_table)

        tempoFine = time()
        print("Hai completato il puzzle in ",tempoFine - tempoInizio)

    else:
        print("SUCA")


if  __name__ == "__main__":
    main()