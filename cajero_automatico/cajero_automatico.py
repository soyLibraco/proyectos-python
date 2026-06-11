from time import sleep

saldo_inicial = 25000.00

while True:
    print()
    print("1. Consultar saldo.")
    print("2. Depositar dinero.")
    print("3. Retirar dinero.")
    print("4. Salir.")
    print()
    sleep(0.5)

    opcion_menu = input("Ingrese el número de la opción a la que desea seleccionar. ")
    sleep(0.5)
    if opcion_menu not in ["1", "2", "3", "4"]:
        print()
        print("La opción elegida no es correcta.")
        print()
        sleep(0.5)
        continue
    if opcion_menu == "1":
        print()
        sleep(0.5)
        print(f"Tu saldo es de ${saldo_inicial}")
        sleep(0.5)
    elif opcion_menu == "2":
        print()
        try:
            deposito = float(input("Defina la cantidad de dinero que desea depositar: "))
        except ValueError:
            print()
            print("Valor ingresado inválido.")
            continue
        if deposito <= 0:
            print()
            print("Valor ingresado inválido.")
            print()
            continue
        sleep(1)
        print(f"Has depositado ${deposito} con éxito.")
        saldo_inicial += deposito
        print()
        sleep(0.5)
        print(f"Su saldo es de: ${saldo_inicial}")
        print()
        sleep(0.5)
    elif opcion_menu == "3":
        print()
        try:
            retiro = float(input("Defina cuánto dinero desea retirar: "))
        except ValueError:
            print()
            print("Valor ingresado inválido.")
            continue
        if saldo_inicial < retiro:
            print()
            print("No tiene saldo suficiente.")
            print()
            continue
        sleep(1)
        print(f"Has retirado ${retiro} con éxito.")
        saldo_inicial -= retiro
        sleep(0.5)
        print()
        print(f"Su saldo ahora es de ${saldo_inicial}")
        sleep(0.5)
    elif opcion_menu == "4":
        print()
        sleep(0.5)
        print("Gracias por utilizar nuestros servicios.")
        break