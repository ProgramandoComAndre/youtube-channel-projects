somar = (lambda x: x+1)
pares = (lambda x: x % 2==0)

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = list(filter(pares,lista))
print(resultado)
