# Cria uma nova lista onde cada elemento da lista original é elevado ao quadrado.
# A lista original permanece inalterada.
def pure_func(List):
    New_list = []
    for i in List:
        New_list.append(i**2)
    return New_list

Lista_original = [1, 2, 3, 4]
Lista_modificada = pure_func(Lista_original)
print(Lista_original)
print(Lista_modificada)

print("-------------------------------------------------------------")

# Função que chama a si mesma em uma soma.
def sum(L, i, n, count):
    # (L): A lista de números a serem somados / (i): O índice atual na lista
    # (n): O tamanho da lista / (count): A soma acumulada até o momento
    if n <= i:
        return count
    # Se o índice atual 'i' for maior ou igual ao tamanho da lista 'n', significa que percorremos todos os elementos.
    # Então retorna 'count'(a soma acumulada)

    count += L[i]
    # Adicionamos o valor do elemento atual L[i] à soma acumulada.
    count = sum(L, i + 1, n, count)
    # Chamamos a função 'sum' recursivamente para o próximo índice i + 1.
    return count

L = [1, 2, 3, 4, 5]
count = 0
n = len(L)
print(sum(L, 0, n , count))     # 15

print("-------------------------------------------------------------")

def gritar(text):
    return text.upper()

def sussurrar(text):
    return text.lower()

def cumprimentar(func):
    greeting = func("Olá! Eu fui criado por uma função de argumento")
    print(greeting)
    # Recebe outra função como argumento (gritar ou sussurrar) e a usa para processar uma mensagem.
cumprimentar(gritar)

print("-------------------------------------------------------------")

def adicao(n):
    return n + n
# Dobra o valor dos números.

nums = (1, 2, 3, 4)
results = map(adicao, nums)
# O 'map' aplica essa função a cada elemento de 'nums', mas 'map' retorna um iterador.
# Então você precisa iterar sobre 'results' para ver os resultados.


print(results)             # <map object at ...>

for result in results:
    print(result, end=" ")      # 2 4 6 8

print("-------------------------------------------------------------")

# Função que filtra vogais.
def fun(variable):
    vogais = ['a', 'e', 'i', 'o', 'u']
    return variable in vogais
# A função 'fun' verifica se um caractere é uma vogal.

sequencia = ['g', 'e', 'e', 'j', 'k', 's', 'r']

filtrando = filter(fun, sequencia)
# O 'filter' usa essa função para filtrar a sequência, retornando apenas as vogais.

print("As letras filtrando sao: ")
for s in filtrando:
    print(s)                        # e e

print("-------------------------------------------------------------")

cubo = lambda x: x*x*x
# A função lambda calcula o cubo de x.

print(cubo(7))                 # 343


L = [1, 2, 3, 4, 5, 6]
pares = [x for x in L if x%2==0]
# Aqui, 'pares' é uma lista que contém apenas os números pares de 'L', usando compreensão de lista.

print(pares)                   # [2, 4, 6]