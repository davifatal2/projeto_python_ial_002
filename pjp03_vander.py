# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:04:14 2020

@author: Thais Helena
"""
import random

from random import randint



def GeraSenha(Tipo, Tam):
    """Gera a senha a ser acrescentada na linha de cada saída do arquivo SENHAS"""
    
    senha_gerada = []
    if Tipo.lower() == "a":
        i = 0
        while i < Tam:
            caracter = randint(48,57)
            senha_gerada.append(chr(caracter))
            i += 1
        senha_string = ""
        for i in senha_gerada:    
            senha_string += i 
             
        return senha_string

    if Tipo.lower() == "b":
        i = 0
        while i < Tam:
            c = randint(1,2)
            if c == 1:
                caracter = randint(65,90)
                senha_gerada.append(chr(caracter))
                i += 1
            else:
                caracter = randint(97,122)
                senha_gerada.append(chr(caracter))
                i += 1
        senha_string = ""        
        for i in senha_gerada:    
            senha_string += i 
             
        return senha_string
    
    if Tipo.lower() == "c":
        i = 0
        while i < Tam:
            c = randint(1,2)
            if c == 1:
                caracter = randint(65,90)
                senha_gerada.append(chr(caracter))
                i += 1
            else:
                caracter = randint(48,57)
                senha_gerada.append(chr(caracter))
                i += 1
        senha_string = ""        
        for i in senha_gerada:    
            senha_string += i 
             
        return senha_string
    
    if Tipo.lower() == "d":
        i = 0
        while i < Tam:
            c = randint(1,3)
            if c == 1:
                caracter = randint(65,90)
                senha_gerada.append(chr(caracter))
                i += 1
            elif c == 2:
                caracter = randint(48,57)
                senha_gerada.append(chr(caracter))
                i += 1
            else:
                caracter = randint(97,122)
                senha_gerada.append(chr(caracter))
                i += 1
        senha_string = ""        
        for i in senha_gerada:    
            senha_string += i 
             
        return senha_string
    
    if Tipo.lower() == "e":
        i = 0
        while i < Tam:
            c = randint(1,4)
            if c == 1:
                caracter = randint(65,90)
                senha_gerada.append(chr(caracter))
                i += 1
            elif c == 2:
                caracter = randint(48,57)
                senha_gerada.append(chr(caracter))
                i += 1
            elif c == 3:
                caracter = randint(97,122)
                senha_gerada.append(chr(caracter))
                i += 1
            else:
                especial = [33,46,58,64]
                caracter = especial[randint(0,3)]
                senha_gerada.append(chr(caracter))
                i += 1
                
        senha_string = ""        
        for i in senha_gerada:    
            senha_string += i 
             
        return senha_string
            

def Leitura_Matriculas():
    """Faz a leitura do arquivo MATR e atribui a uma variável"""
    arquivo = open("MATR.txt", "r")
    dados = arquivo.readline()
    matriculas = []
    while dados != "":
        dados = dados.rstrip()
        t = dados.split()
        matriculas.append(t)
        dados = arquivo.readline()
    arquivo.close()
    return matriculas

def SenhaAluno ():
    """Inicia o programa e gera a saída com as matriculas e as senhas no arquivo SENHAS"""
    
    print("***************GERADOR DE SENHAS***************\n")
    print("Tipos de senhas:\n\na. Numérica\nb. Alfabética\nc. Alfanumérica1\nd. Alfanumérica2\ne. Geral\n")
    Tipo = input("Informe a letra correspondente ao tipo de senha:")
    tipos = ["a","b","c","d","e","A","B","C","D","E"]
    while Tipo not in tipos:
        Tipo = input("Informe a letra correspondente ao tipo de senha:")
        
    Tamanho = int(input("Informe o tamanho da senha a ser gerada:"))
        
    matriculas = Leitura_Matriculas()
    

    arquivo = open("SENHAS.txt", "w")
    for n in matriculas:
        senha = GeraSenha(Tipo, Tamanho)
        arquivo.write("{};{};\n".format(n[0],senha))
    arquivo.close()      

SenhaAluno()           
        
                                                                    
    
    
    
    
    
    
    

    
        


           