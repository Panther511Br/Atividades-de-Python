numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in numeros:
    if x%2 == 0:
        print(x)

numeros.append(11)
numeros.append(12)
numeros.append(13)
numeros.remove(5)

numeros.reverse()

print(numeros)

print("---------------------------------------------------")

dados = (10, 20, 30, 40, 50)
y = dados[2]
print(y)

dados[0] = 15 #Tuplas não podem ser alteradas, senão dará erro

print("---------------------------------------------------")

aluno = {"Nome": "Oswaldo",
         "Idade": 20,
         "Nota": 8.7}

aluno.update({"Nota": 9})
aluno["Curso"] = "Ciencias da Computação"
aluno.pop("Idade")

print(aluno)

print("---------------------------------------------------")

def soma(a,b):
    return a+b

lista = [10, 20, 30, 40]
def media(lista):
    media_lista = sum(lista) / len(lista)
    print(f"Média da lista: {media_lista}")

media(lista)

def eh_par(numero):
    return numero % 2 == 0

print(eh_par(6))
print(eh_par(5))
    
