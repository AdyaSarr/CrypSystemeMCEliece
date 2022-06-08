# -*- coding: utf-8 -*- 
import params

Fq = []
FqPoly = []
FqBinai = []
def corpsFinisPolynome(nombre, premier, puiss):
    print("F"+str(nombre)+"=F"+str(premier)+"[X]/<P(X)>")
    print(params.converBinaiPoly("{0:b}".format(params.primitif[4])))
    print("F"+str(nombre)+"={q(X) ∈ F"+str(premier)+" telle que dq<"+str(puiss)+"}")
    for i in range(nombre):
        Fq.append(i)
    print("==============================Representation Decimale===================================")
    print('F'+str(nombre)+" = ",Fq)
    for i in range(nombre):
        FqBinai.append("{0:b}".format(Fq[i]))
    print("==============================Representation Binaire===================================")
    print('F',nombre," = ",FqBinai)
    for i in range(nombre):
        conca = ""
        tab = FqBinai[i]
        temp = (len(tab)-1)
        for j in tab:
            if temp == 0:
                if j == str(1):
                    conca = conca + j
            elif j=="1" and len(tab)>=2:
                conca = conca + "X^" + str(temp) + "+"
            temp = temp -1
            if conca == "":
                conca = str(0)
        if conca[-1] == "+":
            conca = conca[:-1]
        FqPoly.append(conca)
    print("==============================Representation Polynomiale===================================")
    print('F'+str(nombre)+" = ",FqPoly)
corpsFinisPolynome(params.q, params.p, params.puissance)