def encrypt(message,encriptmsg):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    newmessag=""
    for char in message:
        x=alphabet.index(char)
        newmessag=newmessag+encriptmsg[x]
        return newmessag

print(encrypt("amo", "yo quiero ir a cuba"))
