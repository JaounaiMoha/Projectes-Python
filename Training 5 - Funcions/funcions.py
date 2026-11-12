
def calcular_preu(preu_peces, cost_ma_obra):
    total = preu_peces + cost_ma_obra
    return total


# Prova de la funcio
preu = calcular_preu(45, 30)
print("Cost total:", preu, "€")


# RESPOSTES

# 1. La funcio te dos parametres: preu_peces i cost_ma_obra.

# 2. Retorna el cost total de la reparacio,
# sumant el preu de les peces i la ma d'obra.

# 3. Si eliminem el return, la funcio no retornaria
# el resultat i la variable preu tindria el valor None.

#Exercici 2

def aplicar_descompte(preu, tipus_client):
    tipus_client = tipus_client.lower()

    if tipus_client == "particular":
        descompte = 0
    elif tipus_client == "empresa":
        descompte = 10
    elif tipus_client == "client habitual":
        descompte = 15
    else:
        print("Error: tipus de client no valid")
        return preu

    preu_final = preu - (preu * descompte / 100)
    return preu_final


print("Particular:", aplicar_descompte(100, "particular"), "€")
print("Empresa:", aplicar_descompte(100, "empresa"), "€")
print("Client habitual:", aplicar_descompte(100, "client habitual"), "€")
print("Client incorrecte:", aplicar_descompte(100, "estudiant"), "€")

#exercici 3

def calcular_iva(preu):
    return preu * 21 / 100


def aplicar_descompte(preu, tipus_client):
    if tipus_client.lower() == "particular":
        return preu
    elif tipus_client.lower() == "empresa":
        return preu * 0.90
    elif tipus_client.lower() == "client habitual":
        return preu * 0.85
    else:
        print("Tipus de client incorrecte")
        return preu

def calcular_factura(preu, tipus_client):
    preu_final = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_final)
    return preu_final + iva


# Proves
print("IVA:", calcular_iva(100), "€")
print("Particular:", calcular_factura(100, "particular"), "€")
print("Empresa:", calcular_factura(100, "empresa"), "€")
print("Client habitual:", calcular_factura(100, "client habitual"), "€")

#exercici 4

# EXERCICI 4. PROGRAMA COMPLET: SERVEI TECNIC

def mostrar_menu():
    print("\n===== SERVEI TECNIC INFORMATIC =====")
    print("1. Introduir una nova reparacio")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturacio acumulada")
    print("4. Sortir")


def introduir_reparacio():
    nom = input("Nom del client: ")
    peces = float(input("Cost de les peces: "))
    ma_obra = float(input("Cost de la ma d'obra: "))
    tipus_client = input("Tipus de client (particular, empresa o client habitual): ")

    preu_inicial = calcular_preu(peces, ma_obra)
    preu_final = aplicar_descompte(preu_inicial, tipus_client)
    descompte = preu_inicial - preu_final
    iva = calcular_iva(preu_final)
    total = calcular_factura(preu_inicial, tipus_client)

    print("\n===== FACTURA =====")
    print("Client:", nom)
    print("Preu inicial:", preu_inicial, "€")
    print("Descompte:", descompte, "€")
    print("IVA (21%):", iva, "€")
    print("Total a pagar:", total, "€")

    return total


def consultar_reparacions(nombre):
    print("Nombre de reparacions realitzades:", nombre)


def consultar_facturacio(facturacio):
    print("Facturacio acumulada:", facturacio, "€")


def iniciar_programa():
    nombre_reparacions = 0
    facturacio_total = 0

    while True:
        mostrar_menu()
        opcio = input("Selecciona una opcio: ")

        if opcio == "1":
            total = introduir_reparacio()
            nombre_reparacions = nombre_reparacions + 1
            facturacio_total = facturacio_total + total

        elif opcio == "2":
            consultar_reparacions(nombre_reparacions)

        elif opcio == "3":
            consultar_facturacio(facturacio_total)

        elif opcio == "4":
            print("Programa finalitzat. Fins aviat!")
            break

        else:
            print("Opcio no valida. Torna-ho a provar.")


iniciar_programa()
