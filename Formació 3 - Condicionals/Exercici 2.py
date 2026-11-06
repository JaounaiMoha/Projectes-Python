num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))
num3 = int(input("Introdueix el tercer nombre: "))

if num1 >= num2 and num1 >= num3:
    print("El nombre més gran és:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El nombre més gran és:", num2)
else:
    print("El nombre més gran és:", num3)