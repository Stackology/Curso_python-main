# Faça um programa qque informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

try:
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        print(f'{num} e par')
    else:
        print(f'{num} e impar')
except:
    print('Nao e um numero inteiro')