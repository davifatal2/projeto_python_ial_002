arquivo = open("ALUNOS.txt", "r")
s = arquivo.readline()
print("Matrícula Nome do aluno            Média Final Situação")

while s != "":  # Laço para ler os dados do arquivo "alunos.txt"
    s = s.rstrip()
    s = s.split(";")
    nome = s[4]  # Leitura do nome do aluno
    media = (4 * float(s[1]) + 4 * float(s[2]) + 2 * float(s[3]))/10
    media = round(media, 1)
    if media >= 6.0:  # Avaliação das notas atribuídas conforme o cálculo da média
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(f'{s[0]} {s[4]:25} {media:5}      {situacao:15}')
    s = arquivo.readline()  # Leitura da próxima linha do arquivo
arquivo.close()
