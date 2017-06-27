

def decrypt(encrypted, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ''
    for char in encrypted:
        if char == ' ':
            decrypted = decrypted + ' '
        else:
            pos = cipher.index(char)
            decrypted = decrypted + alphabet[pos]
    return decrypted


cipher = "badcfehgjilknmporqtsvuxwzy"

encrypted = encrypt('hello world', cipher)
print encrypted

decrypted = decrypt(encrypted, cipher)
print(decrypted)
