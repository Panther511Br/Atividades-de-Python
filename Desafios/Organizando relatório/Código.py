# Executar no Google Colab

import re
from google.colab import files

# Upload do arquivo
print("Faça upload do arquivo:")
uploaded = files.upload()
nome_arquivo = list(uploaded.keys())[0]

# Leitura e processamento
linhas_processadas = []
with open(nome_arquivo, 'r', encoding='utf-8') as f:
    texto = f.read()  # Leitura do conteúdo completo
    f.seek(0)  # Volta ao início para ler linha a linha
    for linha in f:
        linha_limpa = linha.strip()
        if linha_limpa:
            linha_formatada = re.sub(r"\s+", " ", linha_limpa).strip().lower().capitalize()
            linhas_processadas.append(linha_formatada)

# Contagem de palavras-chave
def contagem(texto, nome):
    print(f"Quantas vezes a palavra '{nome}' aparece:")
    texto_dividido = texto.lower().split()
    print(texto_dividido.count(nome))

palavras_chave = ["erro", "sucesso", "falha", "cliente", "produto"]

for palavra in palavras_chave:
    contagem(texto, palavra)

# Impressão de frases relevantes
print("\nFrases que contêm palavras-chave:")
frases_relevantes = []
for frase in linhas_processadas:
    if any(p in frase.lower() for p in palavras_chave):
        frases_relevantes.append(frase)
        print("•", frase)

# Geração do novo arquivo
with open("relatorio_processado.txt", "w", encoding="utf-8") as f:
    for linha in linhas_processadas:
        f.write(linha + "\n")

# Download do arquivo
print("\n✅ Download do arquivo limpo:")
files.download("relatorio_processado.txt")
