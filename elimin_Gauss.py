#!/usr/bin/python3.5
#coding: utf-8


class Matriz(object):
    def __init__(self,linEcol):
        self.linEcol = linEcol
        self.matriz = Matriz

    def Cria(self,linEcol):
        Matriz = [0] * linEcol

        for i in range(linEcol):
            Matriz[i] = [0]*(linEcol+1)

        return Matriz

    def Exibe(self, Matriz, linEcol):
        for i in range (linEcol):
            print("| ",end="")
            for j in range (linEcol+1):
                if j != linEcol:
                    print (Matriz[i][j]," ",end="")
                else:
                    print (" | ",Matriz[i][j], end="")
                    print (" |")

    def Preenche(self, Matriz, linEcol):
        for i in range(linEcol):
            for j in range(linEcol+1):
                print("ELEMENTO LINHA ",i," E COLUNA ",j)
                Matriz[i][j] = int(input("-->"))

    def Gauss(self, Matriz, linEcol):
        A = []
        k = 0
        for i in range (linEcol):
            for j in range (1+k,linEcol):
                print("PRIMEIRO - ",Matriz[i][i]," SEGUNDO - ",Matriz[j][i],"\t---",Matriz[i][i]/Matriz[j][i])
                A.append(Matriz[i][i]/Matriz[j][i])
            k = k+1
        print(A)
        k = 0
        for i in range (1+k,linEcol):
            for j in range (linEcol+1):
                Matriz[i][j] = A[k]*Matriz[i][i]
            k = k+1
        return Matriz


linEcol = int(input("quantas linhas e colunas?"))

#CRIAR FUNÇÃO QUE LÊ DO ARQUIVO

###___MAIN___
M = Matriz(linEcol)
print(M.linEcol)
M.matriz = M.Cria(linEcol)
M.Exibe(M.matriz, M.linEcol)
M.Preenche(M.matriz, M.linEcol)
M.Exibe(M.matriz, M.linEcol)
M.Gauss(M.matriz, M.linEcol)
M.Exibe(M.matriz, M.linEcol)

