import time
import os


string = input("Digite um valor")

stringAtual = ""

for i in string:
    os.system("cls")# Linux: clear Windows: cls
    stringAtual += i
    print(stringAtual)
    time.sleep(1)

input()
