#!/usr/bin/python3.5
#coding: utf-8
import sys

class CorDeFundo(object):
    vermelho = '\033[41m'
    verde = '\033[42m'
    azul = '\033[44m'
    ciano = '\033[46m'
    magenta = '\033[45m'
    amarelo = '\033[43m'
    branco = '\033[47m'
    preto = '\033[40m'

class CorDaLetra(object):
    vermelho ='\033[31m'
    verde ='\033[32m'
    azul ='\033[34m'
    ciano ='\033[36m'
    magenta ='\033[35m'
    amarelo ='\033[33m'
    preto ='\033[30m'
    branco ='\033[37m'
    original ='\033[0;0m'
    reverso ='\033[2m'
    negrito = '\033[1m'

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
            print(CorDaLetra.vermelho,"| ",end="")
            for j in range (linEcol+1):
                if j != linEcol:
                    print (Matriz[i][j]," ",end="")
                else:
                    print (" | ",Matriz[i][j], end="")
                    print (" |",CorDaLetra.original)

    def Preenche(self, Matriz, linEcol):
        for i in range(linEcol):
            for j in range(linEcol+1):
                print("ELEMENTO LINHA ",i," E COLUNA ",j)
                Matriz[i][j] = int(input("-->"))

    def Pivo(self, Matriz, linEcol):
        A = []
        k = 0
        for i in range (linEcol):
            for j in range (1+k,linEcol):
                if Matriz[i][i] != 0:
                    print(CorDaLetra.azul,"PRIMEIRO - ",Matriz[i][i]," SEGUNDO - ",Matriz[j][i],"\t---",Matriz[i][j]/Matriz[i][i],CorDaLetra.original)
                    A.append(Matriz[j][i]/Matriz[i][i])
            k = k+1
        print(A)

        return A


    def Gauss(self, Matriz, linEcol, pivo):
        k = 0
        q = 0
        for c in range (1,linEcol):
            print ("------------------------------------ c --> ",c )
            M.Exibe(M.matriz, M.linEcol)

            for i in range (c,linEcol):
                for j in range (k,linEcol+1):
                    Matriz[i][j] = Matriz[i][j] - ( pivo[q]*Matriz[c-1][j] )
                q = q+1
            pivo = M.Pivo(M.matriz, M.linEcol)
            k = k+1


        return Matriz

    def LeArquivo(self,Matriz):

        temp = []
        nome = sys.argv[2]
        arq = open(nome, 'r')
        for line in arq:
            convertido = float(line)
            temp.append(convertido)
        arq.close()

        k = 1
        for i in range(linEcol):
            for j in range(linEcol+1):
                print("ELEMENTO LINHA ",i," E COLUNA ",j)
                Matriz[i][j] = temp[k]
                k = k + 1


#CRIAR FUNÇÃO QUE LÊ DO ARQUIVO

###___MAIN___
linEcol = int(input("quantas linhas e colunas?"))
M = Matriz(linEcol)
print(M.linEcol)
M.matriz = M.Cria(linEcol)
M.Exibe(M.matriz, M.linEcol)
auto = sys.argv[1]

if auto:
    M.LeArquivo(M.matriz)
else:
    M.Preenche(M.matriz, M.linEcol)

M.Exibe(M.matriz, M.linEcol)
Pivo = M.Pivo(M.matriz, M.linEcol)
M.Gauss(M.matriz, M.linEcol, Pivo)
M.Exibe(M.matriz, M.linEcol)

