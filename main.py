import os
import time
from web3 import Web3
import getpass
import src.rsa as rsa
import src.banner as banner
import src.fernet as fernet
import src.logECC as logECC
import src.ciphCesar as ciphCesar
import src.smartcontract as smartcontract


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
    '''
    # Configuración de la conexión y contrato inteligente
    network_url = str(input("URL de tu red ethereum"))
    contract_address = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"
    # Datos de la cuenta del remitente
    sender_address = str(input("Direccion remitente"))
    private_keyETH = getpass.getpass("Llave privada remitente")
    # Conexión a la red de Ethereum
    w3 = smartcontract.connect_to_ethereum(network_url)
    # Cargar el contrato inteligente
    contract = smartcontract.load_contract(w3, contract_address)
    '''
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
            cipher_text = ciphCesar.encrypt(message, disp)
            '''tx_hash = smartcontract.send_text(w3, contract, text_to_send, sender_address, private_keyETH)'''
            print("Mensaje cifrado:", cipher_text)
        # Metodo asimetrico
        elif ciphMeth == 2:
            private_key, public_key = rsa.generate_key_pair()
        
            rsa.save_private_key(private_key, f'keys/{username}_privk.pem')
            rsa.save_public_key(public_key, f'keys/{username}_pubk.pem')

            private_key = rsa.load_private_key(f'keys/{username}_privk.pem')
            public_key = rsa.load_public_key(f'keys/{username}_pubk.pem')

            message = str(input("Mensaje: "))
            cipher_text = rsa.encrypt(public_key, message)
            '''tx_hash = smartcontract.send_text(contract, text_to_send, sender_address, private_keyETH)'''
            print("Mensaje cifrado:\n", cipher_text)
        # Metodo extra
        elif ciphMeth == 3:
            fernet.generate_key(username)
            key = fernet.load_key(username)

            message = str(input("Mensaje: "))
            cipher_text = fernet.encrypt(message, key)
            '''tx_hash = smartcontract.send_text(contract, text_to_send, sender_address, private_keyETH)'''
            print("Mensaje cifrado:\n", cipher_text)
        else:
            print("Accion no valida")
    else:
        print("Inicio de sesión fallido")
else:
    print("Acción no válida")
