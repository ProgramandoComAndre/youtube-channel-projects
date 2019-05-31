import sys
import os

class Contacto:
    
    def __init__(self,formatacao = "",nome = "",numero = ""):

        if nome == "" and numero == "" and formatacao != "":
            
            split = formatacao.split(",")
            self.nome = split[0]
            self.numero = split[1]
        elif formatacao == "" and nome != "" and numero != "":
            self.nome = nome
            self.numero = numero

    def formatacao(self):
        return self.nome +","+self.numero





def dadosPreenchidos(*argv):
    dados = list(filter(lambda x: x != "",argv))
    return len(dados) == len(argv)

def lerPalavraPasse(ficheiro):
    file = open(ficheiro,"r")
    return file.read()


def dialogoSaida(string):
    sair = input(string).lower()
    if sair == "s":
        return True
    return False

def contactoExiste(contacto):
    listaContactosExiste = list(filter((lambda x:x.nome == contacto.nome and x.numero == contacto.numero),listaContactos))
    return len(listaContactosExiste) > 0


def isPhoneNumber(numero):
    return len(numero) == 9 and numero.isnumeric()
        
def criarContacto():
    global listaContactos
    ficheiroContactos = open("Contactos.txt","a")
    
    while True:
        nome = input("Digite o nome do contacto")
        numero = input("Digite o numero")
        

        if not isPhoneNumber(numero) or not dadosPreenchidos(nome,numero):
            print("Erro a criar contacto")
            continue
  
        contacto = Contacto(nome = nome,numero = numero)
        if not contactoExiste(contacto):
            
            ficheiroContactos.write(contacto.formatacao()+"\n")
            listaContactos.append(contacto)
            ficheiroContactos.close()
            break
        else:
            print("Este contacto já existe")
            
def criarPalavraPasse(requerPalavraPasse = False):
    file = open("password.txt","w")
    palavraPasse = ""
    repeticao = ""
    while not dadosPreenchidos(palavraPasse,repeticao) and requerPalavraPasse:
        palavraPasse = input("Digite a palavra passe: ")
        repeticao = input("Digite novamente a palavra passe: ")
        if palavraPasse == repeticao:
            file.write(palavraPasse)        
        else:
            palavraPasse = ""
            repeticao = ""
    file.close()
    return palavraPasse

password = ""      

if os.path.isfile("password.txt"):
    password = lerPalavraPasse("password.txt")
else:
    password = criarPalavraPasse(requerPalavraPasse = dialogoSaida("Deseja palavra passe?(s ou n)"))


listaContactos = []

"""
Ler o ficheiro dos contactos


"""

ficheiroContactos = None
try:
    ficheiroContactos = open("Contactos.txt","r")
    for i in ficheiroContactos.readlines():
        contacto = Contacto(formatacao = i.strip())
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
    for i,j in enumerate(listaContactos):
        print(str(i)+"-"+j.formatacao())





    



def atualizarAgenda():
    ficheiro = open("Contactos.txt","w")
    for i in listaContactos:
        ficheiro.write(i.formatacao()+"\n")
    ficheiro.close()





    
    
def eliminarContacto():
    mostrarContactos()

    sair = False
    while not sair:
        string = input("Digite os identificadores(n1,n2,n3,n4,n5)")
        identificadores = string.split(",")
        identificadores = map(int,identificadores)
        identificadores = list(identificadores)
        global listaContactos
        listaContactos = list(filter(lambda x: not listaContactos.index(x) in identificadores,listaContactos))
        atualizarAgenda()
        sair = not dialogoSaida("Deseja eliminar mais contactos?")

        
        
        
        

         


def editarContacto(identificador,nome,numero):




    if isPhoneNumber(numero):
        
        contactoTeste = Contacto(nome = nome,numero = numero)
    
        if not contactoExiste(contactoTeste):
            listaContactos[identificador].nome = nome
            listaContactos[identificador].numero = numero
            atualizarAgenda()
        else:
            print("Os dados já existem")
    else:
        print("Erro a criar contacto")



functions = {"1":mostrarContactos,"2":criarContacto,"3":sys.exit,"4":eliminarContacto,"5":editarContacto}

while teclado != "3":
    teclado = input("1-Ver Contactos 2- Criar contacto 3-sair 4-Eliminar Contacto editar-(5,id,nome,numero)")
    try:
        executar = functions[teclado]
        executar()
    except:
        tecladoSplit = teclado.split(",")
        if "5" in tecladoSplit and len(tecladoSplit) == 4:
            if dadosPreenchidos(tecladoSplit[1],tecladoSplit[2],tecladoSplit[3]):
                identificador = int(tecladoSplit[1])
                nome = tecladoSplit[2]
                numero = tecladoSplit[3]
                functions[tecladoSplit[0]](identificador,nome,numero)
            else:
                print("Dados não preenchidos")
        elif "5" in tecladoSplit[0] and len(tecladoSplit) != 4:
            print("Argumentos insuficientes")
        else:
            print("Opcao invalida")


    
