from time import sleep

def menu():
    print()
    print("--------------------------------")
    print("1. Consultar saldo.")
    print("2. Depositar dinero.")
    print("3. Retirar dinero.")
    print("4. Ver historial de movimientos.")
    print("5. Salir.")
    print("--------------------------------")
    print()
    sleep(0.5)

def opcion_menu():
    opcion = input("Ingrese el número de la opción a la que desea seleccionar. ")
    sleep(0.5)
    if opcion not in ["1", "2", "3", "4", "5"]:
        print()
        print("La opción elegida no es correcta.")
        print()
        sleep(0.5)
        return None
    return opcion
        
def mostrar_saldo(saldo):
    print()
    sleep(0.5)
    print(f"Tu saldo es de ${saldo}")
    sleep(0.5)
    return saldo

def depositar_saldo(saldo):
    print()
    try:
        deposito = float(input("Defina la cantidad de dinero que desea depositar: "))
    except ValueError:
        print()
        print("Valor ingresado inválido.")
        return saldo
    if deposito <= 0:
        print()
        print("Valor ingresado inválido.")
        print()
        return saldo
    sleep(1)
    print(f"Has depositado ${deposito} con éxito.")
    saldo += deposito
    print()
    sleep(0.5)
    print(f"Su saldo es de: ${saldo}")
    print()
    sleep(0.5)
    historial.append(f"Depósito: {deposito}")
    return saldo

def retirar_saldo(saldo):
    print()
    try:
        retiro = float(input("Defina cuánto dinero desea retirar: "))
    except ValueError:
        print()
        print("Valor ingresado inválido.")
        return saldo
    if retiro <= 0:
        print()
        print("Valor ingresado inválido.")
        print()
        return saldo
    elif saldo < retiro:
        print()
        print("No tiene saldo suficiente.")
        print()
        return saldo
    sleep(1)
    print()
    print(f"Has retirado ${retiro} con éxito.")
    saldo -= retiro
    sleep(0.5)
    print()
    print(f"Su saldo ahora es de ${saldo}")
    sleep(0.5)
    historial.append(f"Retiro: {retiro}")
    return saldo

def mostrar_historial(historial):
    if len(historial) == 0:
        print()
        sleep(0.5)
        print("Todavía no hay movimientos.")
    else:
        for movimiento in historial:
            print()
            sleep(0.5)
            print(movimiento)


def salida():
    print()
    sleep(0.5)
    print("Gracias por utilizar nuestros servicios.")
    print()

saldo = 25000.00
historial = []

while True:

    menu()

    opcion = opcion_menu()
    if opcion is None:
        continue

    if opcion == "1":
        mostrar_saldo(saldo)

    elif opcion == "2":
        saldo = depositar_saldo(saldo)

    elif opcion == "3":
        saldo = retirar_saldo(saldo)

    elif opcion == "4":
        mostrar_historial(historial)
    
    elif opcion == "5":
        salida()
        break