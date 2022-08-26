#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:29:07 2022

@author: root
"""
class matrix:
    def __init__(self,nbr_row,nbr_col): #initialisation de la matrice
        self.nbr_row = nbr_row
        self.nbr_col = nbr_col       
        mat=[]
        for i in range(nbr_row):
            ligne = []
            for j in range(nbr_col):
                ligne.append(0)
            mat.append(ligne)
        self.matrix = mat
    def load(self,tableau): #permet de convertir un 2d-array en matrice
        if len(tableau) != self.nbr_row or len(tableau[0]) != self.nbr_col:
            return ("error : Bad dimensions")
        for i in range(self.nbr_row):
            for j in range(self.nbr_col):
                self.matrix[i][j]=tableau[i][j]
                
    def __getitem__(self,index):
        return self.matrix[index]
 
    def __setitem__(self,index,value):
        self.matrix[index]=value
     
    def __repr__(self):#Representation matricielle
        repres=""
        for i in range(self.nbr_row):
            repres=repres+str(self.matrix[i])
            if i != self.nbr_row-1:
                repres=repres+"\n"
        return repres
    
    def move_in(self): #permet d'entrer les valeurs des éléments de la matrice en float
        print("\n")       
        print("Definition des valeurs de la matrice avec comme adresse: "+str(hex(id(self))))
        print("--------------------------------------------------------"+"\n")       
        for i in range(self.nbr_row):
            for j in range(self.nbr_col):
                x=float(input("ligne:"+str(i)+" colonne:"+str(j)+" : "))
                if x==int(x):
                    x=int(x)
                self[i][j]=x
        print("\n")

    def identity(self):  #charge l'identité dans la matrice si elle est carrée
        if self.nbr_row != self.nbr_col:
            return ("error : l'identité est une matrice carrée")
        for i in range(self.nbr_row):
            for j in range(self.nbr_col):
                if i==j:
                    self[i][j]=1
                else:
                    self[i][j]=0
    #Operations sur les matrices
    
    def __len__(self):#permet de retourner la taille de la matrice
        return self.nbr_col*self.nbr_row
    
    def couple_row_colomn(self):#permet de donner le couple (nombre de ligne, nombre de colonne)
        return(self.nbr_row,self.nbr_col)
    
    def permutation_lignes(self,ligne1,ligne2): #permutation de deux lignes entre elles
        if not isinstance(ligne1,int) or not isinstance(ligne2,int):
            return("error : Vous devez entré deux entiers")
        matreturn = matrix(self.nbr_row,self.nbr_col)
        for i in range(self.nbr_row):
            if i==ligne1:
                matreturn[i]=self[ligne2]
            elif i==ligne2:
                matreturn[i]=self[ligne1]
            else:
                matreturn[i]=self[i]
        return matreturn
    
    def transpose(self): #renvoie la matrice transposée
        matreturn = matrix(self.nbr_col,self.nbr_row)
        for i in range(self.nbr_col):
            for j in range(self.nbr_row):
                matreturn[i][j]=self[j][i]
        return matreturn
    
    def column(self,ind): #renvoie le ind^ème vecteur colonne
        matreturn=matrix(self.nbr_row,1)
        for i in range(self.nbr_row):
            matreturn[i][0]=self[i][ind]
        return matreturn
    
    def lign(self,ind): #revoie le ind^ème vecteur ligne
        matreturn=matrix(1,self.nbr_col)
        for i in range(self.nbr_col):
            matreturn[0][i]=self[ind][i]
        return matreturn
    
    def __add__(self,other):#permet d'ajouter deux matrice de meme taille
        if not isinstance(other,matrix):
            return ("error : S'il vous plait entré une matrice")
        if (self.nbr_row != other.nbr_row or self.nbr_col != other.nbr_col):
            return ("error : Les matrices doivent avoir les memes dimensions")
        mat = matrix(self.nbr_row,self.nbr_col)
        for i in range(self.nbr_row):
            for j in range(self.nbr_col):
                mat[i][j]=int(self[i][j]+other[i][j])%2
        return mat

    def __sub__(self,other):
        if not isinstance(other,matrix):
            return ("error : S'il vous plait entré une matrice")
        if (self.nbr_row != other.nbr_row or self.nbr_col != other.nbr_col):
            return ("error : Les matrices doivent avoir les memes dimensions")
        matreturn = matrix(self.nbr_row,self.nbr_col)
        for i in range(self.nbr_row):
            for j in range(self.nbr_col):
                matreturn[i][j]=int(self[i][j]-other[i][j])%2
        return matreturn
    
    def __mul__(self,other):#la multiplication de  deux matrices
        matreturn = matrix(self.nbr_row,self.nbr_col)         
        if isinstance(other,matrix):
            if (self.nbr_col != other.nbr_row):
                return ("error: les dimensions ne sont pas bonne")           
            for i in range(self.nbr_row):
                for j in range(self.nbr_col):
                    x=0
                    for ind in range(self.nbr_col):
                        x=int(x+self[i][ind]*other[ind][j])%2
                    matreturn[i][j]=x
        else:
            for i in range(self.nbr_row):
                for j in range(self.nbr_col):
                    matreturn[i][j]=int(other*self[i][j])%2
        return matreturn
    
    def __pow__(self,exposant):   #la puissance est définie pour les exposants entiers relatifs
        if not isinstance(exposant,int):
            return ("error : l'exposant doit etre un entier relatif")
        if self.nbr_row != self.nbr_col:
            return ("error : ce n'est pas une matrice carrée")
        if exposant==0:
            matreturn = matrix(self.nbr_row,self.nbr_col)
            matreturn.identity()           
            return matreturn
        if exposant>0:
            matreturn = matrix(self.nbr_row,self.nbr_col)
            matreturn.identity()
            for i in range(exposant):
                matreturn = matreturn*self
            return matreturn
        if exposant==-1:
            if self.nbr_row!=self.nbr_col:
                return("error : tu dois inversé une matrice carrée")
            ident=matrix(self.nbr_row,self.nbr_col)
            ident.identity()           
            matinter=self.augment_c(ident)        
            mat1=matinter.gauss_jordan()
            matreturn=mat1.slice_c(self.nbr_col,mat1.nbr_col+1)
            return matreturn
         
        if exposant<-1:
            return (self**(-1))**(-exposant)
    
    def gauss_jordan(self): #renvoie la matrice échelonnée réduite
        line, col = self.nbr_row, self.nbr_col
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
        for i in range(self.nbr_row):
            for j in range(self.nbr_col):
                if tab[i][j]==int(tab[i][j]):
                    tab[i][j]=int(tab[i][j])
        matreturn=matrix(self.nbr_row,self.nbr_col)
        matreturn.load(tab)
        return matreturn
    
    def matrice_standard(self):
        matreturn = matrix(self.nbr_row, self.nbr_col)
        for i in range(self.nbr_row):
            for j in range(self.nbr_col):
                pivot = matreturn.lign(i)
                pivot2 = matreturn.lign(i+1)
                if pivot[0] == 0:
                    matreturn = matreturn.permutation_lignes(i, i+1)
                    pivot = matreturn.lign(i)
                pivot2[0][j] = int((int(pivot[0][j])+int(matreturn[i+1][j]))%2)
        for i in range(self.nbr_row):
            matreturn.append(pivot2)
        return matreturn