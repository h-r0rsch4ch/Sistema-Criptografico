def encrypt(message, disp):
    cipherText = ""
    for character in message:
        if character.isalpha():
            code = ord(character)
            cipherCode = (code - ord('a') + disp) % 26 + ord('a')
            cipherChar = chr(cipherCode)
            cipherText += cipherChar
        else:
            cipherText += character
    return cipherText


def decrypt(cipherText, disp):
    decoText = ""
    for character in cipherText:
        if character.isalpha():
            code = ord(character)
            decoCode = (code - ord('a') - disp) % 26 + ord('a')
            decoChar = chr(decoCode)
            decoText += decoChar
        else:
            decoText += character
    return decoText
