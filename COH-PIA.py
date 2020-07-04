import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def total_palavras (lista_de_palavras):
    total = 0
    for a in lista_de_palavras:
        total = total + len(a)
    return total    

def total_frases (lista_de_frases):
    total = 0
    for a in lista_de_frases:
        total = total + len(a)
    return total    

def total_caracteres_frases (lista_de_frases):
    total = 0
    ia = 0
    ib = 0
    while ia < len(lista_de_frases):
        for a in lista_de_frases[ib]:
            total = total + len(a)
        ia += 1
        ib += 1
    return total    


def contador_caracteres(lista):
    c = 0
    for a in lista:
        c = c + len(a)
    return c 


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    modulo = 0
    while i < 6 :
      modulo = modulo + abs(as_a[i] - as_b[i])
      i += 1
    return modulo / 6
    
    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_frases = []
    for a in separa_sentencas(texto):
        lista_frases.append(separa_frases(a))
    ia = 0
    ib = 0
    lista_palavras = []
    while ia < len(lista_frases):
        for a in lista_frases[ib]:
            lista_palavras.append(separa_palavras(a))
        ib += 1
        ia += 1
    i = 0
    lista_final = []
    while i < len(lista_palavras):
        lista_final = lista_final + lista_palavras[i]
        i += 1
    
    tamanho_medio_frase = total_caracteres_frases (lista_frases) / contador_caracteres(lista_frases)
    complexidade_sentenca = total_frases(lista_frases) / len(separa_sentencas(texto))
    tamanho_medio_sentenca = contador_caracteres(separa_sentencas(texto)) / len (lista_frases)
    tamanho_medio_palavra = contador_caracteres(lista_final) / len(lista_final)
    hapax_legomana = n_palavras_unicas(lista_final) / len(lista_final)
    type_token = n_palavras_diferentes(lista_final) / len(lista_final)
      
    return [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca,
            complexidade_sentenca, tamanho_medio_frase]


   
        
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    i = 0
    while i < len(textos):
        assinaturas.append(calcula_assinatura(textos[i]))
        i += 1
    i2 = 0
    i3 = 0
    
    sab = []
    menor = 1000     
    while i2 < len(assinaturas):   
        sab.append(compara_assinatura(ass_cp,assinaturas[i2]))
        i2 += 1
    while i3 < len(sab):
        if sab[i3] < menor:
           menor = sab[i3]
           final = i3 + 1
           
        else:
           i3 = i3 + 1 
    return final    
        
def inicio ():
    ass_cp = le_assinatura()
    lista_textos = le_textos()
    resultado = avalia_textos(lista_textos,ass_cp)
    print("\nO autor do texto {}  está infectado com COH-PIAH".format(resultado))

inicio()
    
    
    

    


