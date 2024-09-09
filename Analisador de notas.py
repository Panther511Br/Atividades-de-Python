nome = str(input("Digite o nome do aluno: "))
AV1 = float(input("Digite a nota AV1: "))
AV2 = float(input("Digite a nota AV2: "))
AV3 = float(input("DIgite a nota AV3: "))

soma = AV1 + AV2 + AV3;
media = soma/3;

if(media >= 6):
    print("Aluno", nome, "esta aprovado com media ", media, "e conceito A.\n")
elif(media < 4):
    print("Aluno", nome, "foi reprovado com media ", media, "e conceito A.\n")
elif(media >= 4 and media < 6):
    print("Aluno em recuperacao.\n")

    AVS = float(input("Digite a nota AVS: "))

    if(media + AVS)/2 >=5:
        print("Aluno", nome, "esta aprovado com media ", (media + AVS)/2, "e conceito B.\n")
    else:
        print("Aluno", nome, "esta reprovado com media ", (media + AVS)/2, "e conceito C.\n")