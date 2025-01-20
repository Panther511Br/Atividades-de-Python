def soma(a, b):
    print(a + b)
    # Recebe dois valores e imprime a soma deles.

n1 = int(input('digite o valor: '))
n2 = int(input('digite o valor: '))
soma(n1, n2)

print("------------------------------------------------")

# Diz o índice do 'valor'.
def pesquise(lista, valor):
    for x, e in enumerate(lista):
    # Percorre a lista com índices.
        if e == valor:
            return x
        #Se e == valor, retorna o índice x.
        return None
        # Se não encontrar o valor, retorna 'None'

valores = [13, 17, 19, 23]
print(pesquise(valores, 19))
print(pesquise(valores, 31))

print("------------------------------------------------")

# Essa conta quantas vezes o 'valor' apareceu na 'lista' e o índice da última ocorrência.
def pesquise(lista, valor):
    count, ult_indice = 0, None
    for x, e in enumerate(lista):
        if e == valor:
            count += 1
            ult_indice = x
        #Se e == valor: 'count' conta +1 e 'ult_índice' recebe o último índice.
    return count, ult_indice

valores = [13, 17, 19, 20]
print(pesquise(valores, 20))
print(pesquise(valores, 45))

print("------------------------------------------------")

# Função que faz uma operação (+, -, *, /) sobre dois números.
def calc(esqd, dirt, op):
    if op == '+':
        return esqd + dirt
    elif op == '-':
        return esqd - dirt
    elif op == '*':
        return esqd * dirt
    elif op == '/':
        return esqd / dirt
esqd = int(input('Digite o primero valor: '))
dirt = int(input('Digite o segundo valor: '))
op = input('digite operador: + ou - ou * ou /: ')

print(calc(esqd, dirt, op))

print("------------------------------------------------")

# Função passa apenas a copia da variável. Não mudando a variavel de verdade.
# Já na lista passa um objeto, que pode ser alterado.

def func1(a):
    a = 13

def func2(lista):
    lista[0] = 13

a = 11
lista = [10, 10, 10]

func1(a)
func2(lista)

print(a)
print(lista)
# 'a' permanece 11 porque 'func1' só alterou uma cópia de 'a'. 
# 'lista' é alterada para [13, 10, 10] porque 'func2' modificou diretamente a 'lista' original.