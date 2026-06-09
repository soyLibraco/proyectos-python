import random

puntos_usuario = 0
puntos_computadora = 0
while True:
    eleccion_usuario = input("Elige tu jugada:\n[Escribe salir para terminar.]").lower()
    if eleccion_usuario == "salir":
        break
    computadora = random.choice(["piedra", "papel", "tijera"])
    print(f"Elección de la máquina: {computadora}")
    
    if eleccion_usuario == computadora:
        print("Empate!")
    elif eleccion_usuario == "piedra" and computadora == "tijera":
        print("Tu Piedra destrozó la Tijera!")
        puntos_usuario = puntos_usuario + 1
    elif eleccion_usuario == "papel" and computadora == "piedra":
        print("Tu Papel envolvió la Piedra!")
        puntos_usuario = puntos_usuario + 1
    elif eleccion_usuario == "tijera" and computadora == "papel":
        print("Tu Tijera hizo jirones el Papel!")
        puntos_usuario = puntos_usuario + 1
    else:
        print("Te acaba de humillar la máquina 😢")
        puntos_computadora = puntos_computadora + 1
    print(f"Marcador -> Tú: {puntos_usuario} | PC: {puntos_computadora}\n")

print("¡Gracias por jugar! Resultado final:")
if puntos_usuario > puntos_computadora:
    print("¡Ganaste la partida! 🏆")
elif puntos_usuario < puntos_computadora:
    print("La máquina ganó la partida 🤖")
else:
    print("¡Empate en la partida! 🤝")