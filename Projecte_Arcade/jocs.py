
import random
import robot


def janken():
    print("\n--- PEDRA, PAPER, TISORA ---")

    print("1. El primer que arribi a 3 victòries")
    print("2. Al millor de 5 rondes")

    mode = input("Escull una opció (1 o 2): ")

    while mode not in ["1", "2"]:
        print("Opció incorrecta!")
        mode = input("Escull una opció (1 o 2): ")

    victories_jugador = 0
    victories_robot = 0
    rondes = 0

    if mode == "1":
        objectiu = 3
    else:
        objectiu = 3

    while victories_jugador < objectiu and victories_robot < objectiu:

        print("\n--- NOVA RONDA ---")

        jugador = input("Escull pedra, paper o tisora: ").lower()

        while jugador not in ["pedra", "paper", "tisora"]:
            print("Opció incorrecta!")
            jugador = input("Torna-ho a intentar: ").lower()

        maquina = robot.jugar()

        print("Tu has escollit:", jugador)
        print("El robot ha escollit:", maquina)

        rondes += 1

        if jugador == maquina:
            print("Empat!")

        elif (jugador == "pedra" and maquina == "tisora") or \
             (jugador == "paper" and maquina == "pedra") or \
             (jugador == "tisora" and maquina == "paper"):

            print("Has guanyat aquesta ronda!")
            victories_jugador += 1

        else:
            print("El robot ha guanyat aquesta ronda!")
            victories_robot += 1

        print("\nPuntuació:")
        print("Jugador:", victories_jugador)
        print("Robot:", victories_robot)

    print("\n--- RESULTAT FINAL ---")

    if victories_jugador > victories_robot:
        print("Has guanyat la partida!")
    else:
        print("El robot guanya la partida...")


def nana():
    print("\n--- ENDEVINAR EL NÚMERO ---")

    numero_secret = random.randint(1, 100)
    intents = 0

    while True:

        try:
            numero = int(input("Endevina un número entre 1 i 100: "))
            intents += 1

            if numero < 1 or numero > 100:
                print("El número ha d'estar entre 1 i 100!")

            elif numero < numero_secret:
                print("Massa baix! Torna-ho a intentar.")

            elif numero > numero_secret:
                print("Massa alt! Torna-ho a intentar.")

            else:
                print("\nFelicitats! Has endevinat el número!")
                print("El número era:", numero_secret)
                print("Has necessitat", intents, "intents.")
                break

        except ValueError:
            print("Has d'introduir un número vàlid!")
