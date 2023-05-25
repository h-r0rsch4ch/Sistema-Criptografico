import base64
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey


# Encriptación
def encrypt(data: bytes, password: bytes) -> bytes:
    encrypted_array = []
    i = 0
    for d in data:
        encrypted_array.append(((d + password[i]) % 256).to_bytes(1, "big"))
        i = (i + 1) % len(password)
    return b''.join(encrypted_array)


# Desencriptación
def decrypt(data: bytes, password: bytes) -> bytes:
    decrypted_array = []
    i = 0
    for d in data:
        decrypted_array.append(((d - password[i]) % 256).to_bytes(1, "big"))
        i = (i + 1) % len(password)
    return b''.join(decrypted_array)


# Escritura de archivos
def write(data: bytes, path: str) -> None:
    with open(path, "wb") as file:
        file.write(data)


# Lectura de archivos
def read(path: str) -> bytes:
    with open(path, "rb") as file:
        return file.read()


# Generación de llaves
def gen_key_pair() -> bytes:
    kp = SigningKey.generate()
    return kp._seed


# Firmado
def sign(msg: str, seed: bytes) -> bytes:
    sign_key = SigningKey(seed)
    signed_raw = sign_key.sign(msg.encode("utf-8"))
    return signed_raw


# Registro
def register(username: str, password: str) -> None:
    seed = gen_key_pair()
    signed = sign(username, seed)
    write(encrypt(seed, password.encode("utf-8")), f"keys/{username}.key")
    write(signed, f"certs/{username}.cer")


# Inicio de sesión
def login(username: str, password: str) -> bool:
    seed = decrypt(read(f"keys/{username}.key"), password.encode("utf-8"))
    signed_raw = read(f"certs/{username}.cer")
    verify_key = SigningKey(seed).verify_key
    try:
        verify_key.verify(signed_raw)
        return True
    except BadSignatureError:
        return False
