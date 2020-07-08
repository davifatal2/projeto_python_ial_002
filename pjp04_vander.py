# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:05:06 2020

@author: Vander Xavier
"""

""" Exercício 4 - Projeto_Ial - com todos os requisitos bônus"""



# importação de biblioteca externa datetime
from datetime import date

# importação de biblioteca externa random
import random 

from random import randint



#função faz a leitura do arquivo de entrada e gera linha com codigo do produto, quantidade de vendas, preço e icms
def gerador_de_venda():
    
    icms = [["São Paulo", 18],["Sudeste e Sul",12],
            ["Zona France de Manaus",0],["Demais UFs",7]]
        
    
    descricao_produtos = []
    arquivo = open("produtos.txt", "r")
    dados = arquivo.readline()
    while dados != "":
        dados = dados.rstrip()
        t = dados.split(";")
        t[0] = int(t[0])
        t[1] = str(t[1])
        t[2] = float (t[2])
        t[3] = float(t[3])
        t[4] = float(t[4])
        descricao_produtos.append(tuple(t))
        dados = arquivo.readline()
    arquivo.close()    
    vendas = []
    codigo = randint(0,14)
    if descricao_produtos[codigo][1] == "U":
        vendas.append(str(descricao_produtos[codigo][0]))
        quantidade_vendida = randint(0,100)
        preco = descricao_produtos[codigo][3] + descricao_produtos[codigo][3]*(descricao_produtos[codigo][4]/100)
        vendas.append("{:.3f}".format(quantidade_vendida))
        diferenca = randint(1,100)
        if diferenca > 35:         
            vendas.append("{:.2f}".format(preco))
        else:
            desconto = randint(-8,8)
            if desconto >= 0:
                preco = preco + preco*desconto/100
                vendas.append("{:.2f}".format(preco))
            else:
                preco = preco - preco*desconto/100
                vendas.append("{:.2f}".format(preco))
    else:
        vendas.append(str(descricao_produtos[codigo][0]))
        quantidade_vendida = randint(0,250) + random.random()
        preco = descricao_produtos[codigo][3] + descricao_produtos[codigo][3]*(descricao_produtos[codigo][4]/100)
        vendas.append("{:.3f}".format(quantidade_vendida))
        diferenca = randint(1,100)
        if diferenca > 35:         
            vendas.append("{:.2f}".format(preco))
        else:
            desconto = randint(-8,8)
            if desconto >= 0:
                preco = preco + preco*desconto/100
                vendas.append("{:.2f}".format(preco))
            else:
                preco = preco - preco*desconto/100
                vendas.append("{:.2f}".format(preco))
    indice_icms = randint(0,3) 
    
    return vendas + icms[indice_icms]

#Função para definir se um ano é bissexto
def anobissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    if ano % 4 != 0 and ano % 400 == 0:
        return True
    else:
        return False


#Função que define o dia da semana    
def DiaSemana(dd, mm, aa):
    d = date(aa, mm, dd)
    return d.weekday()



#Função para  coletar uma data no formato [dia,mês,ano]        
def coleta_datas():        
        data = []
        meses = [[1,31],[2,29],[3,31],[4,30],[5,31],[6,30],
                 [7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]
                                       
        periodo_dia = int(input("Dia:")) 
        while periodo_dia < 1 or periodo_dia> 31:
            periodo_dia = int(input("Dados Inválidos. \nDia:"))
        data.append(periodo_dia)
        
        periodo_mes = int(input("Mês:")) 
        while periodo_mes < 1 or periodo_mes > 12 or periodo_dia > meses[periodo_mes - 1][1]:
            periodo_mes = int(input("Dados Inválidos. \nMês:"))
        data.append(periodo_mes)
        
        
        if periodo_mes == 2 and periodo_dia == 29:
            periodo_ano = int(input("Ano:"))
            while periodo_ano < 2016 or periodo_ano > 2020 or anobissexto(periodo_ano) == False:
                periodo_ano = int(input("Dados Inválidos. \nAno:")) 
        else:        
            periodo_ano = int(input("Ano:"))
            while periodo_ano < 2016 or periodo_ano > 2020:
                periodo_ano = int(input("Dados Inválidos. \nAno:"))
    
        data.append(periodo_ano) 
        return data 

#Função coleta e compara datas de inicio e final do relatório de vendas        
def periodo_de_vendas():
    
    print("\nInforme a data inicial.")
    data_inicial = coleta_datas()
    
    data_valida = False
    while data_valida == False:
        print("\nInforme a Data Final.")
        data_final = coleta_datas()
        if data_final[2] > data_inicial[2]:
            data_valida = True
        elif data_final[2] == data_inicial[2]:
            if data_final[1] > data_inicial[1]:
                data_valida = True
            elif data_final[1] == data_inicial[1]:
                if data_final[0] >= data_inicial[0]:
                    data_valida = True
                else:
                    data_valida = False
                    print("Dados Inválidos")
            else:
                data_valida = False
                print("Dados Inválidos")
        else:
            data_valida = False
            print("Dados Inválidos")
    return [data_inicial,data_final]    
        

#Função calcula a diferença de datas e gera a quantidade de dias do relatorio
#entrada - uma lista com duas datas e a quantidade de vendas representada por um inteiro       
def registro_de_vendas(x,y):
    
    linha_de_venda = []
    
    meses = [[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],
             [7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]
    
    descricao_produtos = []
    arquivo = open("produtos.txt", "r")
    dados = arquivo.readline()
    while dados != "":
        dados = dados.rstrip()
        t = dados.split(";")
        t[0] = int(t[0])
        t[1] = str(t[1])
        t[2] = float (t[2])
        t[3] = float(t[3])
        t[4] = float(t[4])
        descricao_produtos.append(tuple(t))
        dados = arquivo.readline()
    arquivo.close()    
    while x[0] != x[1]:
        if x[0][2] < x[1][2]:
            while x[0][2] < x[1][2]:
                 while x[0][1] <= 12:
                     while x[0][0] <= meses[x[0][1]-1][1]:
                         if DiaSemana(x[0][0],x[0][1],x[0][2]) != 6:
                             i = 0
                             while i < y:
                                 print(str(x[0][0]),str(x[0][1]),str(x[0][2]),gerador_de_venda())
                                 linha_de_venda.append(x[0] + gerador_de_venda())
                                 i += 1
                             i = 0    
                             x[0][0] += 1
                         else:
                             x[0][0] += 1
                     x[0][0] = 1    
                     x[0][1] += 1
                 x[0][1] = 1 
                 x[0][2] += 1
        elif x[0][2] == x[1][2] and x[0][1] == x[1][1]:
            while x[0][0] < x[1][0]:
                if DiaSemana(x[0][0],x[0][1],x[0][2]) != 6:
                    i = 0
                    while i < y:
                        print(str(x[0][0]),str(x[0][1]),str(x[0][2]),gerador_de_venda())
                        linha_de_venda.append(x[0] + gerador_de_venda())
                        i += 1
                    i = 0    
                    x[0][0] += 1
                else:
                    x[0][0] += 1
        elif x [0][2] == x[1][2]:
            while x[0][1] < x[1][1]:
                while x[0][0] <= meses[x[0][1]-1][1]:
                    if DiaSemana(x[0][0],x[0][1],x[0][2]) != 6:
                        i = 0
                        while i < y:
                            print(str(x[0][0]),str(x[0][1]),str(x[0][2]),gerador_de_venda())
                            linha_de_venda.append(x[0] + gerador_de_venda())
                            i += 1
                        i = 0
                        x[0][0] += 1
                    else:    
                        x[0][0] += 1
                x[0][1] += 1
                x[0][0] = 1
    if DiaSemana(x[0][0],x[0][1],x[0][2]) != 6:
        i = 0
        while i < y:
            print(str(x[0][0]),str(x[0][1]),str(x[0][2]),gerador_de_venda())
            linha_de_venda.append(x[0] + gerador_de_venda())
            i += 1
            
        return linha_de_venda                        
            
    
            
# Função para iniciar o programa 
def relatorio():   
    
    print("***************RELATÓRIO DE VENDAS***************")
    qtde_vendas_dia = int(input("Informe a Quantidade Diária de Vendas:"))
    datas_vendas = periodo_de_vendas()
    registro_arquivo = registro_de_vendas(datas_vendas,qtde_vendas_dia)   
    
    arquivo = open("gravacao.txt", "w")
    for n in registro_arquivo:
        n[2],n[0] = n[0],n[2]
        arquivo.write("{};{:02d};{:02d};{};{};{};{};{};\n".format(n[0],n[1],n[2],
                                                                  n[3],n[4],n[5],n[6],n[7])) 
    arquivo.close()
    return registro_arquivo

    
relatorio()  
    
    
    
    
