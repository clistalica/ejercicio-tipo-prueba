import funciones as fn

def menu():
    flag = True

    print('Bienvenido al sistema de Automotora "Auto Seguro"')
    while flag:
        print("Seleccione la opcion a ejecutar(1 - 4).")
        print("1) Ingresar un Vehiculo nuevo")
        print("2) Buscar un Vehiculo ingresado")
        print("3) Imprimir Certificado")
        print("4) Buscar un Vehiculo ingresado")
        op = int(input(""))

        if op == 1:
            fn.ingresarVehiculo()
        if op == 3:
            fn.imprimirCertificado()
        if op == 4:
            flag = fn.salir()
            