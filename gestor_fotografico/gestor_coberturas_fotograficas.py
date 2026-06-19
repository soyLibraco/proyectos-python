from time import sleep

def menu():
    sleep(0.5)
    print("\n=== Gestor de Coberturas Fotográficas ===")
    print("\n---------------------")
    print("1 - Agregar cobertura")
    print("2 - Ver coberturas")
    print("3 - Buscar coberturas")
    print("4 - Ver estadísticas")
    print("5 - Salir")
    print("---------------------")

def opcion_menu():
    sleep(0.5)
    opcion = input("\nIngrese el número de la opción que desea seleccionar. : ")
    sleep(0.5)
    if opcion not in ["1", "2", "3", "4", "5"]:
        print("\nLa opción elegida no es correcta.")
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
    cobertura = [
        nombre_evento,
        nombre_cliente,
        tipo_evento,
        cantidad_fotos,
    ]
    return cobertura

def mostrar_cobertura(cobertura):
    sleep(0.5)
    print(f"\nNombre: {cobertura[0]}")
    print(f"Nombre del cliente: {cobertura[1]}")
    print(f"Tipo de evento: {cobertura[2]}")
    print(f"Cantidad de fotos: {cobertura[3]}")

def buscar_cobertura(coberturas, palabra):
    encontradas = []
    for cobertura in coberturas:
        if (
            palabra in cobertura[0].lower()
            or palabra in cobertura[1].lower()
            or palabra in cobertura[2].lower()
        ):
            encontradas.append(cobertura)
            sleep(0.5)
            print(f"\nNombre: {cobertura[0]}")
            print(f"Nombre del cliente: {cobertura[1]}")
            print(f"Tipo de evento: {cobertura[2]}")
            print(f"Cantidad de fotos: {cobertura[3]}")
    if len(encontradas) == 0:
        print("\nNo se encontraron coberturas.")

def ver_estadisticas(coberturas):
    if len(coberturas) == 0:
        sleep(0.5)
        print("\nNo hay coberturas cargadas.")
        return
    total_coberturas = len(coberturas)
    total_fotos = 0
    tipos = {}

    for cobertura in coberturas:
        tipo_evento = cobertura[2]
        cantidad_fotos = cobertura[3]
        total_fotos += cantidad_fotos
        if tipo_evento in tipos:
            tipos[tipo_evento] += 1
        else:
            tipos[tipo_evento] = 1
    promedio = total_fotos / total_coberturas
    print("\n===== ESTADÍSTICAS =====")
    print(f"\nCoberturas cargadas: {total_coberturas}")
    print(f"\nFotografías totales: {total_fotos}")
    print(f"\nPromedio de fotos por cobertura: {promedio:.2f}")
    print("\nCoberturas por tipo:")
    print()
    for tipo in tipos:
        print(f"- {tipo}: {tipos[tipo]}")

def salida():
    sleep(0.5)
    print("\n----------------------------------------------------------")
    print("Gracias por utilizar el Gestor de Coberturas Fotográficas.")
    print("----------------------------------------------------------")

def main():
    coberturas = [
            ["Todos los Fuegos", "Christian", "Recital", 848],
            ["Rada & the Colibriquis", "Radagast", "Recital", 765],
            ["Festival de Invierno", "Municipalidad de Paraná", "Evento Cultural", 523],
            ["Expo Educación 2025", "Consejo General de Educación", "Institucional", 412],
            ["Acto Apertura Ciclo Lectivo", "Consejo General de Educación", "Institucional", 287],
            ["Lanzamiento de Campaña", "Juan Pérez", "Campaña Política", 356],
            ["Sesión de Fotos Empresarial", "Panadería Piacere", "Corporativo", 124],
            ["Casamiento Sofía y Martín", "Sofía y Martín", "Casamiento", 1950],
            ["Fiesta de Egresados Promo 2025", "Escuela Normal", "Social", 1368],
            ["Encuentro de Robótica", "Consejo General de Educación", "Institucional", 489]
        ]
    while True:
        menu()
        opcion = opcion_menu()
        if opcion is None:
            continue

        if opcion == "1":
            nombre_evento, nombre_cliente, tipo_evento, cantidad_fotos = obtener_datos()
            cobertura = agregar_cobertura(
                nombre_evento,
                nombre_cliente,
                tipo_evento,
                cantidad_fotos
            )
            coberturas.append(cobertura)

        elif opcion == "2":
            if len(coberturas) == 0:
                print("\nTodavía no hay coberturas cargadas.")
            else:
                for cobertura in coberturas:
                    mostrar_cobertura(cobertura)

        elif opcion == "3":
            sleep(0.5)
            palabra = input("\nIngrese una palabra para buscar: ").lower()
            resultado = buscar_cobertura(coberturas, palabra)
        
        elif opcion == "4":
            sleep(0.5)
            ver_estadisticas(coberturas)

        elif opcion == "5":
            salida()
            break

main()