medias = []
# É uma lista que vai armazenar todas as médias dos alunos.
soma = 0
# Vai acumular a soma de todas as médias, para calcular a média da turma.

while True:
    nome = input("Nome: ")
    if nome == "-1":
        break
# O loop while True vai executar até encontrar a condição de parada.

    n1 = float(input("Nota da primeira prova: "))
    n2 = float(input("Nota da segunda prova: "))
    media = (n1 + n2) / 2

    if media >= 7:
        print("O aluno %s foi aprovado com média %.2f\n" % (nome, media))
    else:
        print("O aluno %s foi reprovado com média %.2f\n" % (nome, media))
# '.2f' significa que mostrará um número float com duas casa decimais depois da vírgula

    soma += media
    # Adiciona a média do aluno à variável 'soma'.
    medias.append(media)
    # Adiciona a média à lista 'medias'.
    
    print("Todas as médias:", medias)
    print("Media da turma: %.2f" % (soma / len(medias)))
    print("Fim!")
