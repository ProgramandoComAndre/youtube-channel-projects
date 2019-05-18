import re
import time
import sys
class Contacto:

    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = str(numero)
        
    
              
    def SaveContact(self,filestream):
        filestream.write(self.nome+","+self.numero+"\n")
    """def mostrarContacto(self):
        print(self.nome+","+self.numero)
    """
    def contactoVazio(self):
        return self.nome == "" or self.numero == ""
    def formatacao(self):
        return self.nome+","+self.numero
    
        

def isPhoneNumber(string):
    try:
        number = int(string)
        if len(string) == 9:
            return True
        else:
            print("Numero invalido")
            return False
    except:
        print("Numero invalido")
        return False
        

def atualizarBaseDados(listaContactos,baseDados):
    
    for i in listaContactos:
        i.SaveContact(baseDados)
    baseDados.close()
    
def criarContacto(listaContactos):

    contacto = Contacto("","")

    testeConversao = False
    contactoExistente = False
    while contacto.contactoVazio() or not testeConversao or contactoExistente:

        
        contacto.nome = ""
        contacto.numero = ""
        contactoExistente = False
        contacto.nome = input("Digite o nome do contacto")
        contacto.numero = input("Digite o numero do seu contacto")
       
        
        testeConversao = isPhoneNumber(contacto.numero)
        if not testeConversao:
            continue
        contactoExistente = contactoExiste(contacto.nome,contacto.numero)


        
            
        

    baseDados = open("contactos.txt","a")
    contacto.SaveContact(baseDados)
    listaContactos.append(contacto)
    baseDados.close()
    
def lerPalavraPasse(ficheiro):
    file = open(ficheiro,"r")
    return file.read()


def criarFicheiroContactos(local):
    ficheiro = open(local+".txt","w")
    return ficheiro

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






        
    


    
    

palavraPass = ""
tentativas = 0
while password != palavraPass and tentativas != 3:
    palavraPass = input("Digite a sua palavra passe")

    if palavraPass != password:
        print("Palavra Passe errada")
        tentativas += 1



if tentativas == 3:
    print("Atingiu o limite de tentativas para entrar no programa.O programa vai fechar")
    time.sleep(3)
    sys.exit()
    
    

print("Bem vindo")
baseDados = None
listaContactos = []
try:
    baseDados = open("contactos.txt","r")
    for line in baseDados:
        strSeparada = line.split(",")
        
        nome = strSeparada[0]
        
        numero = strSeparada[1]

        

        
        searchBarraN = re.search("\n",numero)
        numero = numero[0:searchBarraN.start()]
        contacto = Contacto(nome,numero)

        if not contacto.contactoVazio():
            listaContactos.append(contacto)
    baseDados.close()
        
    
    
    
except(FileNotFoundError):
    baseDados = criarFicheiroContactos("contactos")


output = ""




def contactoExiste(nome,numero):
    for i in listaContactos:
            if i.nome == nome and i.numero == numero:
                print("Esse contacto já existe.")
                return True
            else:
                return False
    
    
def eliminarContactos():
    mostrarContactos()
    while True:

        
        try:
            listaInicial = listaContactos
            string = input("Digite os identificadores a eliminar(n1,n2,n3,n4...)")
            listaIdentificadors = string.split(",")
            listaIdentificadors = list(map(int,listaIdentificadors))
            listaIdentificadors.sort(reverse = True)
            print(listaIdentificadors)

            for i in listaIdentificadors:
                del listaContactos[i]
                
                    
                        
                
                    
            contactos = open("contactos.txt","w")
            
            break
        except(ValueError):
             print("O identificador que digitou é inválido")
        except(IndexError):
             print("O identificador não existe. Todos identificadores que estão depois deste não foram eliminados")

def mostrarContactos():
    for i in range(len(listaContactos)):
            print(str(i)+"-"+listaContactos[i].formatacao())
def editarContacto():
    
    try:

        while True:
            mostrarContactos()
            identificador = input("Digite o identificador(exit para sair)")
            if identificador.lower() == "exit":
                break
            identificador = int(identificador)
            opcao = ""
            while opcao != "exit":
                print("Nome-1 Numero-2 ou exit para sair")
                opcao = input("Digite uma opcao").lower()
                if opcao == "1":
                    contactoExistente = True
                    
                    novoNome = ""

                    while novoNome == "" or contactoExistente:
                        novoNome = ""
                        novoNome = input("Digite um novo nome")
                        contactoExistente = contactoExiste(novoNome,listaContactos[identificador].numero)
                    listaContactos[identificador].nome = novoNome

                    
                    ficheiro = open("contactos.txt","w")
                    atualizarBaseDados(listaContactos,ficheiro)
                    
                    
                elif opcao == "2":
                    novoNumero = "" 
                    testeConversao = False
                    
                    while novoNumero == "" or not testeConversao:
                        novoNumero = input("Digite um novo numero")
                        testeConversao = isPhoneNumber(novoNumero)
                        


                        
                    listaContactos[identificador].numero = novoNumero
                    
                    ficheiro = open("contactos.txt","w")
                    atualizarBaseDados(listaContactos,ficheiro)
                elif opcao != "exit":
                    print("Não existe essa opcao")
                
        
    except(ValueError):
        print("O identificador que digitou é inválido")
    except(IndexError):
        print("O identificador não existe. Todos identificadores que estão depois deste não foram eliminados")
      
while output.lower() != "exit":
    output = input("1-ver contactos,exit(escrever exit),2-criar contacto,3-Eliminar contactos,4-Editar contacto")
    if output == "1":
        mostrarContactos()
        
    elif output == "2":
        criarContacto(listaContactos)
    elif output == "3":
        eliminarContactos()
    elif output == "4":
        if len(listaContactos) != 0:
            editarContacto()
        else:
            print("Tem de criar contactos para poder editar.")
        
        
    else:
        if output.lower() != "exit":
            print("Nao existe esse comando")
    
    
    
