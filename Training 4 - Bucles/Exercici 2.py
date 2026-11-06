nota = 0
hi_ha_un_deu = False

while nota != -1:
    nota = float(input("Introdueix una nota (-1 per acabar): "))

    if nota == 10:
        hi_ha_un_deu = True

if hi_ha_un_deu:
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")