#BlackJack
import random

carta_banco = random.randint(1,10)
totale_banco = carta_banco
print("Carta_banco: ", carta_banco)

carta_player_1 = random.randint(1,10)
carta_player_2 = random.randint(1,10)
totale_player = carta_player_1 + carta_player_2

print(f"Carta 1: {carta_player_1}, carta 2: {carta_player_2}\nTotale: {totale_player}")

perso = False
carta = input("Vuoi una carta? Y/N\n")
if carta == "Y":
    carta = True
else:
    carta = False

while not perso and carta:

    new_card = random.randint(1,10)
    totale_player += new_card

    print(f"New_card: {new_card}\nTotale {totale_player}")

    if totale_player > 21:
        perso = True
    else:
        carta = input("Vuoi una carta? Y/N\n")
        if carta == "Y":
            carta = True
        else:
            carta = False

if not perso:
    while totale_banco <= 17:
        new_card = random.randint(1,10)
        totale_banco += new_card

        print(f"New_card: {new_card}\nTotale {totale_banco}") 

    if totale_banco > 21:
        print("HAI VINTO")
    elif totale_player > totale_banco:
        print("HAI VINTO")
    elif totale_player <= totale_banco:
        print("HAI PERSO")
else:
    print("HAI PERSO")