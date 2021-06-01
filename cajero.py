saldo= 10000
cuenta="0595"
clave="0098"
print(f"****** \nPara poder Ingresar la cuenta es\n{cuenta}\ny la clave es\n{clave}\n******")
def verificacion():
    if(input("Ingrese su cuenta\n")== cuenta):
        print(f"La cuenta es {cuenta}")
        if(input("Ingrese la clave de acceso\n")==clave):
            print("La clave es correcta")
            return True
        else:
            print("La clave no es valida por favor ingrese por ultima vez antes de salir del programa")
            if (input("Ingrese la clave de acceso\n") == clave):
                print("La clave es correcta")
                return True
            else:
                print("Clave incorrecta, hasta luego")
    else:
        print("parecieras que no perteneces a este banco, primero hagase su cuenta con nosotros.gracias")
        return False
def cajero(saldo):

    if(verificacion()==True):
        print(f"Tu saldo disponible es {saldo}")
        monto=int(input("Ingrese el monto que desees retirar\n"))
        if(monto<=saldo):
            saldo -= monto
            print(f"Tu retiro fue exitoso\ny su saldo restante es de {saldo}\n gracias por usar nuestro servicio")

cajero(saldo)