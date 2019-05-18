import time
import os


string = "Hello world"
newString = ""
for i in string:
    os.system("cls")
    newString += i
    print(newString)
    
    time.sleep(2)
