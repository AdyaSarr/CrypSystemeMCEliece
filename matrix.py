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
                print(self[i][j])
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
        matreturn = matrix(self.nbr_row,self.nbr_col)
        for i in range(self.nbr_col):
            for j in range(self.nbr_row):
                matreturn[i][j]=self[j][i]
        return matreturn
    
    def column(self,ind): #renvoie le ind^ème vecteur colonne
        matreturn=matrix(self.nl,1)
        for i in range(self.nl):
            matreturn[i][0]=self[i][ind]
        return matreturn
    
    def lign(self,ind): #revoie le ind^ème vecteur ligne
        matreturn=matrix(1,self.nbr_col)
        for i in range(self.nbr_col):
            matreturn[0][i]=self[ind][i]
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
                pivot2[j] = int((int(pivot[j])+int(matreturn[i+1][j]))%2)
        return matreturn