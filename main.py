import os
import time
import getpass
import src.rsa as rsa
import src.banner as banner
import src.fernet as fernet
import src.logECC as logECC
import src.ciphCesar as ciphCesar


# Limpieza de pantalla
def clearScreen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


# Verificacion de directorios keys/certs
if os.path.isdir("certs/") == False:
    os.mkdir("certs")
if os.path.isdir("keys/") == False:
    os.mkdir("keys")

banner.show_banner()

print("Introduce '1' si deseas registrarte o '2' si deseas iniciar sesión")
first_action_check = int(input())

# Registro
if first_action_check == 1:
    username = input("User: ")
    password = getpass.getpass()
    logECC.register(username, password)
# Inicio de sesion
elif first_action_check == 2:
    username = input("User: ")
    password = getpass.getpass()
    if logECC.login(username, password):
        print("Se ha iniciado sesión correctamente")
        time.sleep(2)
        clearScreen()
        print("Para cifrar un mensaje antes debes seleccionar un metodo de encriptado.\n1. Simetrico.\n2. Asimetrico.\n3. Fernet")
        ciphMeth = int(input())
        # Metodo simetrico
        if ciphMeth == 1:
            message = str(input("Mensaje: "))
            disp = 3
            cipherText = ciphCesar.encrypt(message, disp)
            print("Mensaje cifrado:", cipherText)

        # Metodo asimetrico
        elif ciphMeth == 2:
            private_key, public_key = rsa.generate_key_pair()
        
            rsa.save_private_key(private_key, f'keys/{username}_privk.pem')
            rsa.save_public_key(public_key, f'keys/{username}_pubk.pem')

            private_key = rsa.load_private_key(f'keys/{username}_privk.pem')
            public_key = rsa.load_public_key(f'keys/{username}_pubk.pem')

            message = str(input("Mensaje: "))
            cipherText = rsa.encrypt(public_key, message)
            print("Mensaje cifrado:\n", cipherText)
        # Metodo extra
        elif ciphMeth == 3:
            fernet.generate_key(username)
            key = fernet.load_key(username)

            message = str(input("Mensaje: "))
            cipherText = fernet.encrypt(message, key)
            print("Mensaje cifrado:\n", cipherText)
        else:
            print("Accion no valida")
    else:
        print("Inicio de sesión fallido")
else:
    print("Acción no válida")
