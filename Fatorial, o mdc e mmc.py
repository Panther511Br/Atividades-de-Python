while True:
# O código entra em um laço infinito while True.
    try:
        numero = int(input('Digite um numero entre 1 e 20: '))

#Calculando o fatorial do numero
        if(numero > 1 and numero < 20):
            break
            # Se o número estiver no intervalo entre 1 e 20 (exclusivo), o laço é interrompido com break.
        else:
            print('Por favor, digite um numero entre 1 e 20.')
        # Caso contrario, uma mensagem é exibida e o laço continua pedindo outra entrada.
    except ValueError:
        print('Por favor, digite um numero inteiro valido.')
    # Se a entrada não for um inteiro válido, uma mensagem de erro é exibida pelo except ValueError.

#Calculando o fatorial
resultado = 1
for i in range(1, numero + 1):
    resultado = resultado * i
#O código inicializa a variável 'resultado' com 1.
#Em seguida, utiliza um laço for para calcular o fatorial do 'número', multiplicando 'resultado' por cada valor de 1 até 'numero'.
print('\nO fatorial eh: ', resultado)

#Calculando o MDC com outro numero, por exemplo 12
# Utilizando o algoritmo de Euclides, o código calcula o MDC entre o fatorial (resultado) e outro número (12).
outro_numero = 12
a, b = resultado, outro_numero
while b:
    a, b = b, a%b
mdc = a

#Calculando o MMC com outro numero, por exemplo 12
# O MMC é calculado pela fórmula (a * b) / MDC(a, b), onde 'a' é o fatorial e 'b' é o outro número (12).
mmc = (resultado * outro_numero) / mdc

print('O Maximo Divisor Comum (MDC) do fatorial e', outro_numero, 'eh:', mdc)
print('O Maximo Divisor Comum (MMC) do fatorial e', outro_numero, 'eh:', mmc)

