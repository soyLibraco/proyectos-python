###
# Trivia.

from time import sleep

sleep(0.5)
print("Bienvenido a esta Trivia sobre cultura general!")
sleep(0.5)

nombre_usuario = input("¿Cómo es tu nombre? ")
puntuacion = 0

sleep(0.5)
print(f"Bien {nombre_usuario}! Pues vamos a ello!")
sleep(0.5)
print("Vamos con la primer pregunta: ")
sleep(0.5)
print("1. ¿Cuál es el planeta más grande del Sistema Solar?")
sleep(0.5)
print()
print("A) Saturno.")
print()
print("B) Júpiter.")
print()
print("C) Neptuno.")
print()
print("D) Marte.")
print()
sleep(0.5)


while True:
    respuesta = input("Elige tu respuesta... ").lower() 
    if respuesta in ["a", "b", "c", "d"]:
        break
    print("La respuesta que elegiste no está entre las opciones. Por favor elige A, B, C o D")
    sleep(0.5)
if respuesta == "b":
    print(f"Felicidades {nombre_usuario}! Has acertado! 🥳")
    puntuacion += 5
else:
    print("Uy! Respuesta incorrecta. 😥")
    puntuacion -= 3
sleep(0.5)
print(f"Tus puntos son: {puntuacion} ")


print("Segunda pregunta: ")
sleep(0.5)
print("2. ¿Quién escribió 'Don Quijote de la Mancha'?")
sleep(0.5)
print()
print("A) Lope de Vega.")
print()
print("B) Miguel de Cervantes.")
print()
print("C) Federico García Lorca.")
print()
print("D) Pablo Neruda.")
print()
sleep(0.5)

while True:
    respuesta = input("Elige tu respuesta... ").lower() 
    if respuesta in ["a", "b", "c", "d"]:
        break
    print("La respuesta que elegiste no está entre las opciones. Por favor elige A, B, C o D")
    sleep(0.5)
if respuesta == "b":
    print(f"Felicidades {nombre_usuario}! Has acertado! 🥳")
    puntuacion += 5
else:
    print("Uy! Respuesta incorrecta. 😥")
    puntuacion -= 3
sleep(0.5)
print(f"Tus puntos son: {puntuacion} ")

print("Tercer pregunta: ")
sleep(0.5)
print("3. ¿En qué año llegó el hombre a la Luna por primera vez?")
sleep(0.5)
print()
print("A) 1965.")
print()
print("B) 1967.")
print()
print("C) 1969.")
print()
print("D) 1971.")
print()
sleep(0.5)

while True:
    respuesta = input("Elige tu respuesta... ").lower() 
    if respuesta in ["a", "b", "c", "d"]:
        break
    print("La respuesta que elegiste no está entre las opciones. Por favor elige A, B, C o D")
    sleep(0.5)
if respuesta == "c":
    print(f"Felicidades {nombre_usuario}! Has acertado! 🥳")
    puntuacion += 5
else:
    print("Uy! Respuesta incorrecta. 😥")
    puntuacion -= 3
sleep(0.5)
print(f"Tus puntos son: {puntuacion} ")

print("Cuarta pregunta: ")
sleep(0.5)
print("4. ¿Qué científico formuló la teoría de la relatividad?")
sleep(0.5)
print()
print("A) Isaac Newton.")
print()
print("B) Galileo Galilei.")
print()
print("C) Nikola Tesla.")
print()
print("D) Albert Einstein.")
print()
sleep(0.5)

while True:
    respuesta = input("Elige tu respuesta... ").lower() 
    if respuesta in ["a", "b", "c", "d"]:
        break
    print("La respuesta que elegiste no está entre las opciones. Por favor elige A, B, C o D")
    sleep(0.5)
if respuesta == "d":
    print(f"Felicidades {nombre_usuario}! Has acertado! 🥳")
    puntuacion += 5
else:
    print("Uy! Respuesta incorrecta. 😥")
    puntuacion -= 3
sleep(0.5)
print(f"Tus puntos son: {puntuacion} ")

print("Quinta pregunta: ")
sleep(0.5)
print("5. ¿Quién pintó la Mona Lisa?")
sleep(0.5)
print()
print("A) Leonardo da Vinci.")
print()
print("B) Pablo Picasso.")
print()
print("C) Miguel Ángel.")
print()
print("D) Vincent van Gogh.")
print()
sleep(0.5)

while True:
    respuesta = input("Elige tu respuesta... ").lower() 
    if respuesta in ["a", "b", "c", "d"]:
        break
    print("La respuesta que elegiste no está entre las opciones. Por favor elige A, B, C o D")
    sleep(0.5)
if respuesta == "a":
    print(f"Felicidades {nombre_usuario}! Has acertado! 🥳")
    puntuacion += 5
else:
    print("Uy! Respuesta incorrecta. 😥")
    puntuacion -= 3
sleep(0.5)
print(f"Y tu resultado final es: {puntuacion} puntos! ")
print()
if puntuacion > 17:
    print("Lo has hecho muy bien!")
elif puntuacion > 12:
    print("No estuvo mal, pero se puede mejorar!")
else:
    print("Estuviste flojo, más suerte la próxima!")
sleep(0.5)
print()
print(f"{nombre_usuario}, gracias por jugar esta Trivia.")