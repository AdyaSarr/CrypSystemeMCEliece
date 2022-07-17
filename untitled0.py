#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 20:08:16 2022

@author: root
"""

class matrix:
    def __init__(self,n,p): #initialisation de la matrice
        self.nl=n
        self.nc=p       
        mat=[]
        for i in range(n):
            ligne = []
            for j in range(p):
                ligne.append(0)
            mat.append(ligne)
        self.matrix=mat
     
    def load(self,tableau): #permet de convertir un 2d-array en matrice
        if len(tableau) != self.nl or len(tableau[0]) != self.nc:
            return ("error : Bad dimensions")
        for i in range(self.nl):
            for j in range(self.nc):
                self.matrix[i][j]=tableau[i][j]
     
    def __getitem__(self,index):
        return self.matrix[index]
 
    def __setitem__(self,index,value):
        self.matrix[index]=value
     
    def __repr__(self):
        repres=""
        for i in range(self.nl):
            repres=repres+str(self.matrix[i])
            if i != self.nl-1:
                repres=repres+"\n"
        return repres
     
    def __add__(self,other):
        if not isinstance(other,matrix):
            return ("error : You must add matrix with matrix")
        if (self.nl != other.nl or self.nc != other.nc):
            return ("error : You must add same dimension matrix")
        mat = matrix(self.nl,self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                mat[i][j]=self[i][j]+other[i][j]
        return mat
 
    def __iadd__(self,other):
        if(self.nl!=other.nl or self.nc!=other.nc):
            return ("error : bad dimensions")
        matreturn=self+other
        return matreturn
     
    def __isub__(self,other):
        if(self.nl!=other.nl or self.nc!=other.nc):
            return ("error : bad dimensions")
        matreturn=self-other
        return matreturn
 
    def __mul__(self,other):
        matreturn = matrix(self.nl,self.nc)         
        if isinstance(other,matrix):
            if (self.nc != other.nl):
                return ("error: bad dimension")           
            for i in range(self.nl):
                for j in range(self.nc):
                    x=0
                    for ind in range(self.nc):
                        x=x+self[i][ind]*other[ind][j]
                    matreturn[i][j]=x
        else:
            for i in range(self.nl):
                for j in range(self.nc):
                    matreturn[i][j]=other*self[i][j]
        return matreturn
 
    def __rmul__(self,other):
        if not isinstance(other,matrix):
            matreturn = matrix(self.nl,self.nc)
            for i in range(self.nl):
                for j in range(self.nc):
                    matreturn[i][j]=other*self[i][j]
            return matreturn
 
    def __sub__(self,other):
        if not isinstance(other,matrix):
            return ("error : You must add matrix with matrix")
        if (self.nl != other.nl or self.nc != other.nc):
            return ("error : You must add same dimension matrix")
        matreturn = matrix(self.nl,self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                matreturn[i][j]=self[i][j]-other[i][j]
        return matreturn
     
    def __eq__(self,other):
        if isinstance(other,matrix):       
            return self.matrix==other.matrix
     
     
    def __pow__(self,exposant):   #la puissance est définie pour les exposants entiers relatifs
        if not isinstance(exposant,int):
            return ("error : parameter must be integer")
        if self.nl != self.nc:
            return ("error : you must use a square matrix")
        if exposant==0:
            matreturn = matrix(self.nl,self.nc)
            matreturn.identity()           
            return matreturn
        if exposant>0:
            matreturn = matrix(self.nl,self.nc)
            matreturn.identity()
            for i in range(exposant):
                matreturn = matreturn*self
            return matreturn
        if exposant==-1:
            if self.nl!=self.nc:
                return("error : you must inverse a square matrix")
            ident=matrix(self.nl,self.nc)
            ident.identity()           
            matinter=self.augment_c(ident)        
            mat1=matinter.gauss_jordan()
            matreturn=mat1.slice_c(self.nc,mat1.nc+1)
            return matreturn
         
        if exposant<-1:
            return (self**(-1))**(-exposant)
             
                 
     
     
    def identity(self):  #charge l'identité dans la matrice si elle est carrée
        if self.nl != self.nc:
            return ("error : identity is square matrix")
        for i in range(self.nl):
            for j in range(self.nc):
                if i==j:
                    self[i][j]=1
                else:
                    self[i][j]=0
     
    def zeros(self):
        for i in range(self.nl):
            for j in range(self.nc):
                self[i][j]=0
     
    def move_in(self): #permet d'entrer les valeurs des éléments de la matrice en float
        print("\n")       
        print("Definition of Matrix at adress: "+str(hex(id(self))))
        print("--------------------------------------------------------"+"\n")       
        for i in range(self.nl):
            for j in range(self.nc):
                x=float(input("li:"+str(i)+" co:"+str(j)+" : "))
                if x==int(x):
                    x=int(x)
                self[i][j]=x
        print("\n")
         
    def __len__(self): #renvoie le nombre total d'éléments
        return self.nl*self.nc
     
    def rank(self): #renvoie le couple (nombre de lignes, nombre de colonnes)
        return(self.nl,self.nc)
     
    def augment_c(self,other): #augmente la matrice avec une autre à droite
        if not isinstance(other,matrix) or self.nl != other.nl:
            return "error : you must augment a matrix with a matrix"
        matreturn = matrix(self.nl,(self.nc+other.nc))
        for i in range(self.nl):
            for j in range(self.nc):
                matreturn[i][j]=self[i][j]
            for j in range(other.nc):
                matreturn[i][self.nc+j]=other[i][j]
        return matreturn
     
    def augment_l(self,other): #augmente la matrice avec une autre en dessous
        if not isinstance(other,matrix) or self.nc != other.nc:
            return "error : you must augment a matrix with a matrix"
        matreturn = matrix(self.nl+other.nl,self.nc)
        for i in range(self.nl):
            matreturn[i]=self[i]
        for i in range(other.nl):
            matreturn[i+self.nl-1]
        return matreturn
     
    def permutation_l(self,ligne1,ligne2): #permutation de deux lignes entre elles
        if not isinstance(ligne1,int) or not isinstance(ligne2,int):
            return("error : You must input two int arguments")
        matreturn = matrix(self.nl,self.nc)
        for i in range(self.nl):
            if i==ligne1:
                matreturn[i]=self[ligne2]
            elif i==ligne2:
                matreturn[i]=self[ligne1]
            else:
                matreturn[i]=self[i]
        return matreturn
     
    def permutation_c(self,colonne1,colonne2): #permutation de deux colonnes entre elles
        if not isinstance(colonne1,int) or not isinstance(colonne2,int):
            return ("error : you must imput two int arguments")
        matreturn = matrix(self.nl,self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                if j==colonne1:
                    matreturn[i][j]=self.matrix[i][colonne2]
                elif j==colonne2:
                    matreturn[i][j]=self.matrix[i][colonne1]
                else:
                    matreturn[i][j]=self.matrix[i][j]
        return matreturn
     
    def dilatation_l(self,ligne,facteur): #dilatation d'une ligne
        if not isinstance(ligne,int):
            return ("error : First argument must be int")
        matreturn = matrix(self.nl,self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                if i==ligne:
                    matreturn[i][j]=self[i][j]*facteur
                else:
                    matreturn[i][j]=self[i][j]
        return matreturn
     
    def dilatation_c(self,colonne,facteur): #dilatation d'une colonne
        if not isinstance(colonne,int):
            return ("error : First argument must be int")
        matreturn = matrix(self.nl,self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                if j==colonne:
                    matreturn[i][j]=self[i][j]*facteur
                else:
                    matreturn[i][j]=self[i][j]
        return matreturn
     
    def transvection_l(self,ligne1,ligne2,facteur): #transvection sur les lignes
        if not isinstance(ligne1,int) or not isinstance(ligne2,int):
            return ("error : arguments 1 and 2 must be integers")
        matreturn = matrix(self.nl,self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                if i==ligne1:
                    matreturn[i][j]=self[i][j]+facteur*self[ligne2][j]
                else:
                    matreturn[i][j]=self[i][j]
        return matreturn
     
    def transvection_c(self,colonne1,colonne2,facteur): #transvection sur les colonnes
        if not isinstance(colonne1,int) or not isinstance(colonne2,int):
            return ("error : arguments 1 and 2 must be integers")
        matreturn = matrix(self.nl,self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                if j==colonne1:
                    matreturn[i][j]=self[i][j]+facteur*self[i][colonne2]
                else:
                    matreturn[i][j]=self[i][j]
        return matreturn
         
    def transpose(self): #renvoie la matrice transposée
        matreturn = matrix(self.nc,self.nl)
        for i in range(self.nc):
            for j in range(self.nl):
                matreturn[i][j]=self[j][i]
        return matreturn
     
    def is_ech(self): #renvoie true si la matrice est échelonnée
        pos=[]
        for i in range(self.nc):
            pos.append(self.nl)           
            for j in range(self.nl):
                if self[j][i]!=0:
                    pos[i]=j
        for i in range(len(pos)-1):
            if pos[i]>pos[i+1]:
                return False
        return True
     
    def is_echred(self): #revoie true si la matrice est échelonnée et réduite
        pos=[]
        for i in range(self.nc):
            pos.append(self.nl)           
            for j in range(self.nl):
                if self[j][i]!=0:
                    pos[i]=j
        for i in range(len(pos)-1):
            if pos[i]>pos[i+1] or pos[i]!=1:
                return False
        if pos[len(pos)-1]!=1:
            return False
        return True
     
    def pivots(self): #renvoie une liste dont chaque élément représente un pivot de la matrice (ligne,colonne,valeur)
        mat=self.gauss_jordan()       
        pos=[]
        for i in range(mat.nc):
            pos.append((mat.nl,i,"nan"))           
            for j in range(mat.nl):
                if mat[j][i]!=0:
                    pos[i]=((j,i,mat[i][j]))
        pivots=[]
        if pos[0][2]!="nan":
            pivots.append(pos[0])
        for i in range(1,len(pos)):
            if pos[i][2]!="nan" and pos[i][0]>pos[i-1][0]:
                pivots.append(pos[i])
        return pivots
     
    def gauss_jordan(self): #renvoie la matrice échelonnée réduite
        line, col = self.nl, self.nc
        i, j = 0, 0
        tab = self.matrix[:]  
        while j < col and i < line:
            tab.sort(reverse=1)
            k = i+1
            max = i
            while k < line:
                if ( abs( tab[k][j] ) > abs( tab[max][j] ) ):
                    max = k
                k = k+1
            if tab[max][j] != 0:
                k = j
                piv = tab[max][j]
                while k < col:
                    tab[max][k] = tab[max][k] * 1. / piv
                    k = k+1
                k = 0
                while k < line:
                    if k != max:
                        t = 0
                        ca = tab[k][j]
                        while t < col:
                            tab[k][t] = tab[k][t] - ca * tab[max][t]
                            t = t+1
                    k = k+1
                i = i+1
            j = j+1   
        tab.sort(reverse=1)
        for i in range(self.nl):
            for j in range(self.nc):
                if tab[i][j]==int(tab[i][j]):
                    tab[i][j]=int(tab[i][j])
        matreturn=matrix(self.nl,self.nc)
        matreturn.load(tab)
        return matreturn
 
    def column(self,ind): #renvoie le ind^ème vecteur colonne
        matreturn=matrix(self.nl,1)
        for i in range(self.nl):
            matreturn[i][0]=self[i][ind]
        return matreturn
     
    def lign(self,ind): #revoie le ind^ème vecteur ligne
        matreturn=matrix(1,self.nc)
        for i in range(self.nc):
            matreturn[0][i]=self[ind][i]
        return matreturn
     
    def slice_l(self,inda,indb): #renvoie une matrice qui est un slice des lignes
        matreturn=matrix(indb-inda-1,self.nc)
        for i in range(matreturn.nl):
            for j in range(matreturn.nc):
                matreturn[i][j]=self[inda+i][j]
        return matreturn
     
    def slice_c(self,inda,indb): #renvoie une matrice qui est un slice des colonnes
        matreturn=matrix(self.nl,indb-inda-1)
        for i in range(matreturn.nl):
            for j in range(matreturn.nc):
                matreturn[i][j]=self[i][inda+j]
        return matreturn