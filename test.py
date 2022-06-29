import numpy.polynomial as ml
def get_poly(indice):
    n = bin(indice)[2:]
    L = [0 for i in range(len(n))]
    for i in range(len(n)):
        L[i] = eval(n[i])
    print(L)
    L.reverse()
    return ml.Polynomial(L)
print(get_poly(842))