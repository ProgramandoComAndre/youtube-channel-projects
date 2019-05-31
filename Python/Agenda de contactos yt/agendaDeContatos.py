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




def contactoExiste(contacto):
    listaContactosExiste = list(filter((lambda x:x.nome == contacto.nome and x.numero == contacto.numero),listaContactos))
    return len(listaContactosExiste) > 0


def isPhoneNumber(numero):
        numeroConvertido = 0
        try:
            numeroConvertido = int(numero)
        except:
            pass
        return len(numero) == 9 and numeroConvertido != 0
        
def criarContacto(file,listaContactos):

    numero = ""
    nome = ""
    while numero == "" and nome == "":
        nome = input("Digite o nome do contacto")
        numero = input("Digite o numero")
        

        if not isPhoneNumber(numero) or numero == "" or nome == "":
            print("Erro a criar contacto")
            numero = ""
            nome = ""
            continue
            
            
        contacto = Contacto(nome,numero)
        
        
        
        if not contactoExiste(contacto):
            
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





    



def atualizarAgenda():
    ficheiro = open("Contactos.txt","w")
    for i in listaContactos:
        ficheiro.write(i.formatacao()+"\n")
    ficheiro.close()
    
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

            atualizarAgenda()

            
            
            break
        except(ValueError):
            print("Erro a digitar identificador")
        except(IndexError):
            print("Não existe um contacto com esse identificador")

        
        
def editarContacto(identificador,nome,numero):




    if isPhoneNumber(numero) and nome != "" and numero != "":
        
        contactoTeste = Contacto(nome,numero)
    
        if not contactoExiste(contactoTeste):
            listaContactos[identificador].nome = nome
            listaContactos[identificador].numero = numero
            atualizarAgenda()
        else:
            print("Os dados já existem")
    else:
        print("Erro a editar contacto")
    
    
    
while teclado != "3":
    teclado = input("1-Ver Contactos 2- Criar contacto 3-sair 4-Eliminar Contacto (editar,id,nome,numero)")
    tecladoSplit = teclado.split(",")
    tecladoSplit[0] = tecladoSplit[0].lower()
    if teclado == "1":
        mostrarContactos()

    elif "EDITAR".lower() in tecladoSplit:
        try:
            identificador = int(tecladoSplit[1])
            nome = tecladoSplit[2]
            numero = tecladoSplit[3]
            editarContacto(identificador,nome,numero)
        except:
            print("Erro a editar contacto")
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

    
