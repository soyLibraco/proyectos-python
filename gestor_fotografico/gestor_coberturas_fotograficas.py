from time import sleep

def menu():
    sleep(0.5)
    print()
    print("=== Gestor de Coberturas Fotográficas ===")
    print()
    print("---------------------")
    print("1 - Agregar cobertura")
    print("2 - Ver coberturas")
    print("3 - Buscar coberturas")
    print("4 - Ver estadísticas")
    print("5 - Salir")
    print("---------------------")

def opcion_menu():
    print()
    sleep(0.5)
    opcion = input("Ingrese el número de la opción que desea seleccionar. : ")
    sleep(0.5)
    if opcion not in ["1", "2", "3", "4", "5"]:
        print()
        print("La opción elegida no es correcta.")
        return None
    return opcion

def obtener_datos():
    print("-------------------------")
    nombre_evento = input("Ingrese el nombre del evento: ")
    print("-------------------------")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    print("-------------------------")
    tipo_evento = input("Ingrese el tipo de evento: ")
    print("-------------------------")
    cantidad_fotos = int(input("Ingrese la cantidad de fotos tomadas: "))
    return nombre_evento, nombre_cliente, tipo_evento, cantidad_fotos

def agregar_cobertura(nombre_evento, nombre_cliente, tipo_evento, cantidad_fotos):
    cobertura = {
        "nombre_evento": nombre_evento,
        "nombre_cliente": nombre_cliente,
        "tipo_evento": tipo_evento,
        "cantidad_fotos": cantidad_fotos,
    }
    return cobertura

def mostrar_cobertura(cobertura):
    sleep(0.5)
    print()
    print(f"Nombre: {cobertura['nombre_evento']}")
    print(f"Nombre del cliente: {cobertura['nombre_cliente']}")
    print(f"Tipo de evento: {cobertura['tipo_evento']}")
    print(f"Cantidad de fotos: {cobertura['cantidad_fotos']}")

def buscar_cobertura(coberturas, palabra):
    encontradas = []
    for cobertura in coberturas:
        if (
            palabra in cobertura["nombre_evento"].lower()
            or palabra in cobertura["nombre_cliente"].lower()
            or palabra in cobertura["tipo_evento"].lower()
        ):
            encontradas.append(cobertura)
            print()
            sleep(0.5)
            print(f"Nombre: {cobertura['nombre_evento']}")
            print(f"Nombre del cliente: {cobertura['nombre_cliente']}")
            print(f"Tipo de evento: {cobertura['tipo_evento']}")
            print(f"Cantidad de fotos: {cobertura['cantidad_fotos']}")
    if len(encontradas) == 0:
        print("No se encontraron coberturas.")

def salida():
    print()
    sleep(0.5)
    print("----------------------------------------------------------")
    print("Gracias por utilizar el Gestor de Coberturas Fotográficas.")
    print("----------------------------------------------------------")
    print()

def main():
    coberturas = []
    while True:
        menu()
        opcion = opcion_menu()
        if opcion is None:
            continue
        if opcion == "1":
            nombre_evento, nombre_cliente, tipo_evento, cantidad_fotos = obtener_datos()
            cobertura = agregar_cobertura(nombre_evento, nombre_cliente, tipo_evento, cantidad_fotos)
            coberturas.append(cobertura)
        elif opcion == "2":
            if len(coberturas) == 0:
                print()
                print("Todavía no hay coberturas cargadas.")
            else:
                for cobertura in coberturas:
                    mostrar_cobertura(cobertura)
        elif opcion == "3":
            print()
            sleep(0.5)
            palabra = input("Ingrese una palabra para buscar: ").lower()
            resultado = buscar_cobertura(coberturas, palabra)
        elif opcion == "5":
            salida()
            break

main()