
import jocs

while True:

    print("\n==============================")
    print("   BENVINGUT/DA AL MINI ARCADE")
    print("==============================")

    print("\n1. Jugar a Pedra, Paper, Tisora")
    print("2. Jugar a Endevinar el Número")
    print("S. Sortir")

    opcio = input("\nEscull una opció: ").lower()

    if opcio == "1":
        jocs.janken()

    elif opcio == "2":
        jocs.nana()

    elif opcio == "s":
        print("\nGràcies per jugar al MINI ARCADE!")
        print("Fins aviat!")
        break

    else:
        print("\nOpció incorrecta! Torna-ho a intentar.")
