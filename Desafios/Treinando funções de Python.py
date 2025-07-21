texto = str(input("Insira um texto qualquer: "))

print("Texto todo maiúsculo:", texto.upper())
print("Texto todo minúsculo:", texto.lower())

texto_dividido = texto.split()
# Dividindo cada palavra do texto

contagem_palavras = 0
contagem_a = texto.count("a")
contagem_A = texto.count("A")
# Variaveis para contar a quantidade de palavras e letras a no texto

for palavra in texto_dividido:
    contagem_palavras += 1    

print("Quantas palavras tem no texto:", contagem_palavras)
print("Quantas letras 'a' tem no texto:", contagem_a + contagem_A)

if texto_dividido:
    print("Primeira palavra do texto:", texto_dividido[0])
    print("Última palavra do texto:", texto_dividido[-1])
else:
    print("Texto vazio. Nenhuma palavra para mostrar.")

texto_dividido.reverse()
texto_invertido = " ".join(texto_dividido)
# Invertendo o texto, concatenando as palavras e armazenando na variavel

print("Texto invertido:", texto_invertido)

trocando_A = texto.replace("a", "@")
trocando_a = trocando_A.replace("A", "@")
print("Trocando 'a' por '@':", trocando_a)