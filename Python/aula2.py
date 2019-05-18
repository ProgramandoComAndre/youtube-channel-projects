from math import sqrt

catetoA = 0
catetoB = 0
hipotenusa = 0

#hipotenusa = raiz quadrada de (catetoA**2 + catetoB**2)

catetoA = float(input("Digite o valor do cateto"))
catetoB = float(input("Digite o valor do cateto"))
hipotenusa = sqrt(catetoA**2+catetoB**2)

print(hipotenusa)
