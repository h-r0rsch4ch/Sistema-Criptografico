from cryptography.fernet import Fernet

# Genera una clave aleatoria para el cifrado
def generate_key(username):
    key = Fernet.generate_key()
    with open(f'keys/fernet_{username}.key', 'wb') as f:
        f.write(key)

# Carga la clave desde un archivo
def load_key(username):
    with open(f'keys/fernet_{username}.key', 'rb') as f:
        key = f.read()
    return key

# Cifra el mensaje utilizando la clave proporcionada
def encrypt(message, key):
    f = Fernet(key)
    cipherMessage = f.encrypt(message.encode())
    return cipherMessage

# Descifra el mensaje utilizando la clave proporcionada
def decrypt(cipherMessage, key):
    f = Fernet(key)
    decryptedMessage = f.decrypt(cipherMessage)
    return decryptedMessage.decode()
