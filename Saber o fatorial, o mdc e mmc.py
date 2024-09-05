while True:
    try:
        numero = int(input('Digite um numero entre 1 e 20: '))

#Calculando o fatorial do numero
        if(numero > 1 and numero < 20):
            break
        else:
            print('Por favor, digite um numero entre 1 e 20.')
    except ValueError:
        print('Por favor, digite um numero inteiro valido.')

#Calculando o fatorial
resultado = 1
for i in range(1, numero + 1):
    resultado = resultado * i

print('\nO fatorial eh: ', resultado)

#Calculando o MDC com outro numero, por exemplo 12
outro_numero = 12
a, b = resultado, outro_numero
while b:
    a, b = b, a%b
mdc = a

#Calculando o MMC com outro numero, por exemplo 12
mmc = (resultado * outro_numero) / mdc

print('O Maximo Divisor Comum (MDC) do fatorial e', outro_numero, 'eh:', mdc)
print('O Maximo Divisor Comum (MMC) do fatorial e', outro_numero, 'eh:', mmc)

