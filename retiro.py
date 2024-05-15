import os
import time
saldo = 12000
while True:
    os.system("cls")
    try:
        print(f"Bienvenido \nsu saldo es ${saldo} \n1)Realizar un retiro \n2)Realizar deposito  \n3)Salir")
        op = int(input("selecióne(1-3): "))
        if op >= 1 and op <= 3:
            try:
                if op  == 1:
                    re = int(input("Ingrese el monto a retirar: "))
                    if re <= saldo:
                        saldo -=  re 
                    else:
                        print("No se puede realizar el retiro ")
                        time.sleep(21)
                elif op == 2:
                    ing= int(input("Ingrese el monto: "))
                    saldo += ing
                elif op == 3:
                    print("Saliendo del programa")
                    break
            except ValueError:
                print("Solo se puede ingresar digitos")
            time.sleep(2)
        else:
            print("Recuerde utilizar las opcione (1-3) ")
            time.sleep(2)
    except ValueError:
        print("Recuerde utilizar las opcione (1-3) ")
        time.sleep(2)