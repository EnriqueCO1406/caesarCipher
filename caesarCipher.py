import string


alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def encrypt():
    
    print("Este es el sistema para el cifrado de cesar\n")
    message = input("Escribe el mensaje que deseas encriptar: ").lower()
    print()
    key = int(input("Introduce la llave: ")) #Key=ROT

    encrypted_message = ""

    for c in message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + key) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c

    print("Tu mensaje encriptado es: ")
    print(encrypted_message)

encrypt()