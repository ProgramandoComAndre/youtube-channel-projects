def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)


def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

def lerPalavraPasse(ficheiro):
    file = open(ficheiro,"r")
    return decrypt("Programando_com_Andre_Youtube_2.0",file.read())

def criarPalavraPasse():
    file = open("password.txt","w")
    palavraPasse = ""
    repeticao = ""
    while repeticao == "" and palavraPasse == "":
        palavraPasse = input("Digite a palavra passe: ")
        repeticao = input("Digite novamente a palavra passe: ")
        if palavraPasse == repeticao:
            encrypted = encrypt("Programando_com_Andre_Youtube_2.0",palavraPasse)
            file.write(encrypted)
            return palavraPasse
        else:
            palavraPasse = ""
            repeticao = ""

password = ""      

try:
    password = lerPalavraPasse("password.txt")
except(FileNotFoundError):
    password = criarPalavraPasse()




palavraPass = ""
while password != palavraPass:
    palavraPass = input("Digite a sua palavra passe")

    if palavraPass != password:
        print("Palavra Passe errada")

print("Bem vindo")
