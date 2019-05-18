def isPrime(x):
    primo = True #
    nDigitos = len(str(x))
    for i in range(2,10**(nDigitos+1)+1):
        if x % i == 0 and x != i:
            primo = False
    return primo


def primes(maximo):
    lista = []
    for i in range(2,maximo+1):
        if isPrime(i):
            lista.append(i)
    return lista


print(len(primes(1000)))
    
        
    
    
        

