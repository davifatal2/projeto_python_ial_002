# projeto_python_ial_002
# Projeto 01 - Christian Cubo
arquivo = open("ALUNOS.txt", "r")
s = arquivo.readline()
print("Matrícula Nome do aluno            Média Final Situação")

while s != "":  # Laço para ler os dados do arquivo "alunos.txt"
    s = s.rstrip()
    s = s.split(";")
    matricula = s[0]  # Leitura do número da matrícula
    n1 = float(s[1])  # Leitura da primeira nota
    n2 = float(s[2])  # Leitura da segunda nota
    trabalho = float(s[3])  # Leitura da nota do trabalho
    nome = s[4]  # Leitura do nome do aluno
    media = (4 * n1 + 4 * n2 + 2 * trabalho)/10
    media = round(media, 1)
    if media >= 6.0:  # Avaliação das notas atribuídas conforme o cálculo da média
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(f'{matricula} {nome:25} {media:5}      {situacao:15}')
    s = arquivo.readline()  # Leitura da próxima linha do arquivo
arquivo.close()

