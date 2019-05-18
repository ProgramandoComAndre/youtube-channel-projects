import re


class Contacto:
    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = str(numero)
    

    def formatacao(self):
        return self.nome +","+self.numero

def lerPalavraPasse(ficheiro):
    file = open(ficheiro,"r")
    return file.read()


def criarContacto(file,listaContactos):

    numero = ""
    nome = ""
    while numero == "" and nome == "":
        nome = input("Digite o nome do contacto")
        numero = input("Digite o numero")
        numeroConvertido = 0
        try:
            numeroConvertido = int(numero)
        except:
            pass

        if len(numero) != 9 or numeroConvertido == 0 or numero == "" or nome == "":
            print("Erro a criar contacto")
            numero = ""
            nome = ""
            continue
            
            
            
        existe = False
        contacto = Contacto(nome,numero)
        for i in listaContactos:
            if i.nome == contacto.nome and i.numero == contacto.numero:
                existe = True
                break

        
        if not existe:
            
            file.write(contacto.formatacao()+"\n")
            listaContactos.append(contacto)
        else:
            print("Este contacto já existe")
            nome = ""
            numero = ""
    

def criarPalavraPasse():
    file = open("password.txt","w")
    palavraPasse = ""
    repeticao = ""
    while repeticao == "" and palavraPasse == "":
        palavraPasse = input("Digite a palavra passe: ")
        repeticao = input("Digite novamente a palavra passe: ")
        if palavraPasse == repeticao:
            file.write(palavraPasse)
            return palavraPasse
        else:
            palavraPasse = ""
            repeticao = ""

password = ""      

try:
    password = lerPalavraPasse("password.txt")
except(FileNotFoundError):
    password = criarPalavraPasse()


listaContactos = []

"""
Ler o ficheiro dos contactos


"""

ficheiroContactos = None
try:
    ficheiroContactos = open("Contactos.txt","r")
    for i in ficheiroContactos:
        split = i.split(",")
        nome = split[0]
        numero = split[1]
        barraN = re.search("\n",numero)
        numero = numero[0:barraN.start()]

        contacto = Contacto(nome,numero)
        listaContactos.append(contacto)
    ficheiroContactos.close()

except:
    ficheiroContactos = open("Contactos.txt","w")
    ficheiroContactos.close()






palavraPass = ""
while password != palavraPass:
    palavraPass = input("Digite a sua palavra passe")

    if palavraPass != password:
        print("Palavra Passe errada")

print("Bem vindo")

teclado = ""



def mostrarContactos():
    for i in range(len(listaContactos)):
        print(str(i)+"-"+listaContactos[i].formatacao())

def eliminarContacto():
    mostrarContactos()

    while True:
        try:
            string = input("Digite os identificadores(n1,n2,n3,n4,n5)")
            identificadores = string.split(",")
            identificadores = map(int,identificadores)
            identificadores = list(identificadores)
            identificadores.sort(reverse = True)
            for i in identificadores:
                del listaContactos[i]
            ficheiro = open("Contactos.txt","w")
            for i in listaContactos:
                ficheiro.write(i.formatacao())
            ficheiro.close()
            break
        except(ValueError):
            print("Erro a digitar identificador")
        except(IndexError):
            print("Não existe um contacto com esse identificador")

        
        
        
while teclado != "3":
    teclado = input("1-Ver Contactos 2- Criar contacto 3-sair 4-Eliminar Contacto")
    if teclado == "1":
        mostrarContactos()
        
    elif teclado == "2":
        
        #Criar o contacto
        ficheiroContactos = open("Contactos.txt","a")
        criarContacto(ficheiroContactos,listaContactos)
        ficheiroContactos.close()
    elif teclado == "4":
        eliminarContacto()
    else:
        if teclado != "3":
            print("Opcao invalida")

    
