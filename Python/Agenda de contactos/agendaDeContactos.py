import sqlite3
import os
import random
import re
def encryptString(string):
    newString = ""
    algorithm = random.randint(3,7)
    for i in string:
        asc = ord(i) + algorithm
        char = chr(asc)
        newString += char
    return (newString,algorithm)
        
        
def decryptString(string,algorithm):
    newString = ""
    for i in string:
        asc = ord(i) -algorithm
        char = chr(asc)
        newString += char
    return newString



def writeFile(password):
    n = len(password[0])
    filename = str(n)
    passwordFile = open(filename+".txt","w")
            
                
    passwordFile.write(str(password[1]))
    passwordFile.write(password[0])
    for i in range(0,100000):
        ch = chr(random.randint(1,100))
        passwordFile.write(ch)
    passwordFile.close()
    
def configuracaoInicial():
    requestPassword = input("Deseja colocar uma palavra passe na sua agenda de contactos")
    if requestPassword.lower() == "s":
        password = input("Digite uma palavra passe")
        passwordConfirmation = input("Digite novamente a palavra passe")
        if password == passwordConfirmation:
            encryptedPassword = encryptString(password)
            
            writeFile(encryptedPassword)




passwordFileExists = False
filename = ""
for r,d,f in os.walk(os.path.dirname(os.path.realpath(__file__))):
    
    for file in f:
        if '.txt' in file:
            passwordFileExists = True
            filename = file
            break

if passwordFileExists:
    file = open(filename,"r")
    searchLen = re.search(".txt",filename)
    passwordLength = int(filename[0:searchLen.start()])
    fileContent = file.read()
    password = input("Digite a sua palavra passe\n")
    passwordFromFile = fileContent[1:passwordLength+1]
    passwordFromFile = decryptString(passwordFromFile,int(fileContent[0]))
    if password == passwordFromFile:
        input("Bem vindo")
    else:
        input("Palavra passe errada")
    
        
    file.close()
    os.remove(filename)
    encryptedPassword = encryptString(passwordFromFile)
    writeFile(encryptedPassword)
    
else:
    configuracaoInicial()
    exit(0)
    
    
    
    
    
            
            



    
    
    

            


