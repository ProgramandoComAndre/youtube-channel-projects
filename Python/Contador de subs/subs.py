import re
import urllib3
from bs4 import BeautifulSoup
import requests




codigo = ""
soup = None
try:
    canal = open("canal.txt","r")
    codigo = canal.readline()
    canal.close()

except:

    codigo = input("Digite o código do teu canal (https://www.youtube.com/channel/xxxxxxxxxxxxxxxxx)")
    canal = open("canal.txt","w")
    canal.write(codigo)
    canal.close()

finally:
    url = "https://www.youtube.com/channel/"+codigo
    page_response = requests.get(url,timeout=5)
    
    soup = BeautifulSoup(page_response.content,'html.parser')
    
    
    
    
    print(page_response.content)
    
    input()

    
        
    
