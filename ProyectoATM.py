import sys
import time
import sleep

balancefile = open("balancefile.txt", "w")
balancefile.write("Tu balance inicial es de $10000.0 \n")
USER_BALANCE = 10000.0
name = input("Introduzca su nombre: ")

i = 3
o = 1

print("Tienes 3 intentos para escribir los datos correctos.")
contador = 0
while contador < 3:
    pin = input("Digite la contraseña: ")
    if pin == "1234":
        print("PIN correcto.")
        contador = 4

    else:
        print("PIN incorrecto. Tienes" ,i-o, "oportunidadaes")
        contador += 1
        if contador == 3:
            sys.exit("Has alcanzado el límite permitido de intentos, por favor comuníquese con el administrador del programa")     

print("\n")
print(name +"," + " " + "Tu balance actual es de: $" + str(USER_BALANCE))
print("\n")

while True:
    opcion=input("Que opcion deseas utilizar?. Escribe su numero correspondiente. \n 1. Depositar saldo. \n 2. Retirar saldo. \n 3. Ver balance de la cuenta. \n 4. Salir del ATM. \n")
    print("")
    if opcion=="Depositar saldo" or opcion== "1":
        x= input("Cuanto dinero deseas depositar?: ")
        USER_BALANCE += float(x)
        print("")
        print (name + "," + " " + "Tu balance actual es de: $" + str(USER_BALANCE))
        print("")
        balancefile.write("Has depositado hacia tu la cantidad de $" + x + "." + " " + "Tu balance actual es de $" + str(USER_BALANCE) +"\n")
        continue
    elif opcion== "Retirar saldo" or opcion== "2":
        y= input("Cuanto dinero deseas retirar?: ")
        if float (y)<=USER_BALANCE:
            USER_BALANCE -= float(y)
            print("")
            print (name + "," + " " + "Tu balance actual es de: $" + str(USER_BALANCE))
            print("")
            balancefile.write("Has retirado desde tu cuenta la cantidad de $" + y + "." + " " + "Tu balance actual es de $" + str(USER_BALANCE) + "\n")
            continue
        else:
            print ("No se puede realizar la accion. No tienes suficiente saldo")
            balancefile.write("El usuario registrado ha sido",name)
    elif opcion== "Ver balance de la cuenta" or opcion== "3":
        print("")
        print ("Tu balance actual es de $" + str(USER_BALANCE))
        print("")
    elif opcion== "Salir del ATM" or opcion== "4":
        print ("Hasta luego",name,"!")
        balancefile.write("El nombre del cliente es " + name +"\n")
        balancefile.close()
        break
    else:
        print ("Aviso! No puedes seleccionar esta opcion")
