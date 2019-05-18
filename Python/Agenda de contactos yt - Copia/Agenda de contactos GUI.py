from tkinter import *
import ctypes

listaContactos = []


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




def criarFicheiroContactos(local):
    ficheiro = open(local+".txt","w")
    return ficheiro

def lerListaContactos():
    baseDados = None

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



def contactoExiste(nome,numero):
    for i in listaContactos:
            if i.nome == nome and i.numero == numero:
                print("Esse contacto já existe.")
                return True
            else:
                return False


            



class Login(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.showV = False
        self.master.geometry("500x300")
        ficheiro = open("password.txt")
        
        self.palavraPasse = ficheiro.read()
        self.create_widgets()


    
    def show(self):
        print("Aqui")
        
        if self.var.get() == 1:
            self.text_palavraPasse["show"] = ""
        else:
            self.text_palavraPasse["show"] = "*"
        
    def create_widgets(self):
        self.text_palavraPasse = Entry(self.master,width = 100,show = "*")
        
        self.var = BooleanVar()
        
        self.label_palavraPasse = Label(self.master,text = "Digite a sua palavra passe")
        self.check_showPassword = Checkbutton(self.master,text = "Mostrar palavra passe",variable = self.var,command = self.show)
        self.check_showPassword.place(x= 100,y = 180)
        self.button_confirmar = Button(self.master,text = "Confirmar", command = self.verifyPassword)
        self.text_palavraPasse.place(x=20, y = 150)
        self.label_palavraPasse.place(x=20,y = 120)
        self.button_confirmar.place(x = 20,y = 180)
        

    def verifyPassword(self):
        print(self.text_palavraPasse["text"])
        if self.palavraPasse == self.text_palavraPasse.get():
            global login
            
            login = True
            self.master.destroy()
            ctypes.windll.user32.MessageBoxW(0,"Bem vindo","Agenda de contactos",0)
            
        else:
            ctypes.windll.user32.MessageBoxW(0,"Palavra passe errada","Agenda de contactos",0)
                                    
    def say_hi(self):
        print("Hi there, everyone!")




class VisualizacaoDosContactos(Frame):

    class CriarContactoDialog:
        def __init__(self,parent):
            top = self.top = Toplevel(parent)
            Label(top, text="Nome").pack()

            self.text_nome = Entry(top)
            self.text_nome.pack(padx=5)
            Label(top, text="Numero").pack()
            self.text_numero = Entry(top)
            self.text_numero.pack(padx=5)
            self.botao_criar = Button(self.top,text = "Criar",command = self.NewContact)
            self.botao_criar.pack()

        def NewContact(self):

            if self.text_nome.get() == "" or self.text_numero.get() == "" or not isPhoneNumber(self.text_numero.get()) or contactoExiste(self.text_nome.get(),self.text_numero.get()):
                
                ctypes.windll.user32.MessageBoxW(0,"Erro a criar contacto","Agenda de contactos",0)
            else:
                contacto = Contacto(self.text_nome.get(),self.text_numero.get())
                listaContactos.append(contacto)
                ficheiro = open("contactos.txt","a")
                contacto.SaveContact(ficheiro)
                self.top.destroy()
        


    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        lerListaContactos()
        self.master.geometry("1280x720")
        
        
       
        self.create_widgets()


    def criarContacto(self):
        dialogo = self.CriarContactoDialog(self.master)
        self.master.wait_window(dialogo.top)
        self.listBox_contactos.delete(0,END)
        for i in listaContactos:
            self.listBox_contactos.insert(END,i.formatacao())
        
        
        
    def create_widgets(self):
        self.listBox_contactos = Listbox(self.master,width = 200,height = 30)
        self.listBox_contactos.pack()
        self.button_criarContacto = Button(self.master,text = "Criar Contacto",command = self.criarContacto)
        self.button_criarContacto.place(x = 30,y = 600)
        for i in listaContactos:
            self.listBox_contactos.insert(END,i.formatacao())


root = Tk()
app = Login(master=root)
app.mainloop()

if login:
    root = Tk()
    app = VisualizacaoDosContactos(master = root)
    app.mainloop()
