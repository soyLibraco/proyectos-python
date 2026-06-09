import random

jugar = "y"
while jugar =="y":
    numero_elegido = random.randint(0, 10)
    intentos = 0

    while True:
        numero_usuario = int(input("Adivina el número: "))
        intentos += 1
        if numero_usuario == numero_elegido:
            print(f"Acertaste! El número era {numero_elegido}")
            print(f"Cantidad de intentos : {intentos}")
            break
        elif numero_usuario < numero_elegido:
            print("Estás abajo, sigue intentando.")
        else:
            print("Estás por encima, intenta otra vez.")

    jugar = input("¿Quieres volver a jugar? (y/n) : ").lower()

print("Bye! Gracias por jugar!")
