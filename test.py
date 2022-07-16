import numpy.polynomial as ml



def get_poly(indice):
    n = bin(indice)[2:]
    L = [0 for i in range(len(n))]
    for i in range(len(n)):
        L[i] = eval(n[i])
    print(L)
    L.reverse()
    return ml.Polynomial(L)
def conversionBinaire(x):
    chainBinaire = ""
    i = 0
    while x!=0:
        i = i+1
        bitt = (27>>i)&1
        chainBinaire +=str(bitt)
        x = x>>i
    return chainBinaire
print(conversionBinaire(27))