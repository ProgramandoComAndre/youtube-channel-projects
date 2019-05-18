import matplotlib.pyplot as plt
import openpyxl
import numpy as np

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
rows = sheet.max_row
fruits = []

for i in range(rows):
    tupla = (sheet["B"][i].value,sheet["C"][i].value)
    fruits.append(tupla)

x = []
y = []
for i in range(len(fruits)):
    x.append(fruits[i][0])
    y.append(fruits[i][1])



ypos = range(len(x))
plt.bar(ypos,y)
plt.xticks(ypos,x)
plt.ylabel("Numero de vendas")
plt.title("Venda de frutas")

plt.show()


    
